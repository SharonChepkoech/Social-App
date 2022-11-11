from unicodedata import name
import uuid
from django.db import models

# A popular local newsroom is creating a social news app where its users can comment and debate on news articles.
#  A user creates a debate on an article, sets time for the debate and and invites one guest at a time to debate against
#  They can also mark the debate as private if they want. As a host, they can kick out the guest and invite another one at
#  their discretion, reschedule the debate to a desired time and end the debate for everyone.

# As a guest, you can accept or reject an invitation, join the debate and leave when you desire to.
# Classes -> User, Debate, News_article, and participants.

# User - id, name, 

# News article - id, title, body, time created, 

# Debate - News article(FK), id, time created, private/public, time ended, time started, 

# Participants - id, debate id(FK),  user id(fk), role(choice(host/ guest)), joined at, left at

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 25)
    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    news_article_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 25)
    body = models.TextField(max_length=99)
    time_created = models.DateTimeField(null = True,blank= True) 
    def __str__(self):
        return (self.title)

PRIVACY_STATUS_CHOICES = (('Private','Private'),('Public','Public'))
class Debate(models.Model):
    title = models.CharField(max_length = 25)
    user =  models.ForeignKey(User,on_delete = models.CASCADE,related_name='debate_user')
    debate_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    news_article = models.ForeignKey(NewsArticle,on_delete = models.CASCADE,related_name='debate_article')
    time_created = models.DateTimeField(null = True,blank= True) 
    time_started = models.DateTimeField(null = True,blank= True) 
    time_ended = models.DateTimeField(null = True,blank= True) 
    debate_status = models.CharField(max_length = 30,choices= PRIVACY_STATUS_CHOICES,null= True)
    def __str__(self):
        return self.title

USER_ROLE_CHOICE = (('Host','Host'),('Guest','Guest'))
class Participant(models.Model):
    participant_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    debate = models.ForeignKey(Debate,on_delete = models.CASCADE,related_name='particiant_debate')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='participant_user')
    role = models.CharField(max_length = 30,choices= USER_ROLE_CHOICE,null= True)
    time_joined = models.DateTimeField(null = True,blank= True) 
    time_left = models.DateTimeField(null = True,blank= True) 
    

# Create your models here.
