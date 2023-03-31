from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=10)

class Player(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    palyer_name=models.CharField(max_length=20)
