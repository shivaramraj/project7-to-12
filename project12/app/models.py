from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=20)

class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=20)
    p_age=models.IntegerField()
    p_url=models.URLField()

