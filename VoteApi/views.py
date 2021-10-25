from re import I
from django.core.checks import messages
from rest_framework.decorators import api_view

from VoteApi.serializers import CandidateSerializer
from .models import Candidate, User, Vote
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import serializers
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

    




@api_view(['GET'])
def login(request):
    email = request.headers['email']
    password = request.headers['password']
    message = "Invalid Credentials"
    if(User.objects.filter(email=email,password=password).exists()):
        user = User.objects.filter(email=email)
        return(Response({"success" : True,"message" : "Logging In","user_id" : user[0].user_id}))

    return(Response({"success" : False,"message" : message}))


@api_view(['POST'])
def create_account(request):
    email = request.data['email']
    password = request.data['password']
    name = request.data['name']
    if(User.objects.filter(email=email).exists()):
        return(Response({"success" : False,"message" : "Email Already Exists"}))
    
    new_user = User(user_name=name,email=email,password=password)
    new_user.save()
    return(Response({"success" : True,"message" : "Account Created","user_id" : new_user.user_id}))


@api_view(['POST'])
def add_candidate(request):
    name = request.data['candidate_name']
    position = request.data['position']
    if(Candidate.objects.filter(candidate_name=name).exists()):
        return(Response({"success" : False,"message" : "Candidate Already Exist"}))
    new_candidate = Candidate(candidate_name = name,position=position)
    new_candidate.save()
    return(Response({"succes":True,"message":"Candidate Registered","candidate_id":new_candidate.candidate_id}))




class Get_Candidates(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@api_view(['POST'])
def cast_vote(request):
    user_id = request.data['user_id']
    candidate_id = request.data['candidate_id']
    position = request.data['position']
    success =False
    message = "Invalid Vote"
    if(User.objects.filter(user_id=user_id).exists()):
        if(not Vote.objects.filter(user_id=user_id,position=position).exists()):
            if(Candidate.objects.filter(candidate_id=candidate_id,position=position).exists()):
                success=True
                message="Vote Casted"
                vote = Vote(candidate_id=candidate_id,user_id=user_id,position=position)
                vote.save()
                vote_count = Candidate.objects.filter(candidate_id=candidate_id)[0].vote_count
                Candidate.objects.filter(candidate_id=candidate_id).update(vote_count=vote_count+1)
                channel_layer = get_channel_layer()
                
                async_to_sync(channel_layer.group_send)("Vote_Count", {
                    "type" : "send.everyone"
                  
                })
                
    return(Response({"success" : success,"message" : message}))