from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_analysis, name='profile-analysis')
]