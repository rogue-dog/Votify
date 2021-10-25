from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from VoteApi import models


class CandidateSerializer(ModelSerializer) : 
    class Meta :
        model = models.Candidate
        fields = ['candidate_name','position','candidate_id','vote_count']