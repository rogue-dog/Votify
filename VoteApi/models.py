from re import I
from django.db import models
import uuid
from django.db.models import query

# Create your models here.







class Candidate(models.Model):
    candidate_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    position = models.CharField(max_length=20)
    candidate_name = models.CharField(max_length=250)
    vote_count = models.IntegerField(default=0)





class Vote(models.Model):
    user_id = models.UUIDField()
    candidate_id = models.UUIDField()
    vote_id = models.UUIDField(default=uuid.uuid4 , primary_key=True)
    position = models.CharField(max_length=250)
    






class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    email = models.CharField(max_length=200)
    
    password = models.CharField(max_length=250)





