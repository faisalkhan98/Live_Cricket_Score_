from django.urls import path, include
from . import views
app_name = 'rss'
urlpatterns = [

    path('rss/', views.index, name="index"),
    path('info/', views.Score, name="info"),
    path('about/', views.about, name="about"),
    path('scorecard/', views.scorecard, name="scorecard"),
    path('schedule/', views.schedule, name="schedule"),
    path('match_details/', views.match_details, name="match_details"),


]
