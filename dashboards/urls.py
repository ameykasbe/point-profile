from django.urls import path
from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path('profile-analysis', views.profile_analysis, name='profile-analysis'),
]
