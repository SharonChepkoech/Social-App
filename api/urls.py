from django.urls import path,include
from rest_framework import routers
from .views import NewsArticleViewset, UserViewset, DebateViewset, ParticipantViewset 


router=routers.DefaultRouter()
router.register(r'users', UserViewset)
router.register(r'debates', DebateViewset)
router.register(r'participants', ParticipantViewset)
router.register(r'newsarticles', NewsArticleViewset)



urlpatterns=[
    path('',include(router.urls)),
]