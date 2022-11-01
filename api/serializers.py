from rest_framework import serializers
from socialapp.models import User, Debate, Participant, NewsArticle

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name")

class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = ("debate_status","news_article","title")

# Participants - id, debate id(FK),  user id(fk), role(choice(host/ guest)), joined at, left at

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("id","user","role","time_joined","time_left")

# News article - id, title, body, time created, 

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ("id","title","body","time")

