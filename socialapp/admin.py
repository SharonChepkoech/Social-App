from django.contrib import admin
from .models import User, NewsArticle, Debate, Participant

class UserAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)
    search_fields = ("title",)

class DebateAdmin(admin.ModelAdmin):
    list_display = ("title", "news_article",)
    search_fields = ("title",)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("user", "debate","role",)
    search_fields = ("user","role")



admin.site.register(User, UserAdmin),
admin.site.register(NewsArticle, NewsArticleAdmin),
admin.site.register(Debate, DebateAdmin),
admin.site.register(Participant, ParticipantAdmin),

# Register your models here.
