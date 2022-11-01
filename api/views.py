from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, DebateSerializer, NewsArticleSerializer, ParticipantSerializer
from socialapp.models import User, Debate, Participant, NewsArticle



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer


class DebateViewset(viewsets.ModelViewSet):
    queryset = Debate.objects.all()
    serializer_class=DebateSerializer


class ParticipantViewset(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class=ParticipantSerializer

class NewsArticleViewset(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
# Create your views here.
