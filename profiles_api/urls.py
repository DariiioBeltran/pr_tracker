from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('users/', 
        views.UserProfileList.as_view(), 
        name='user-list'),
    path('users/<int:pk>/', 
        views.UserProfileDetail.as_view(), 
        name='userprofile-detail'),
    path('users/<int:pk>/lifts/',
        views.UserProfileLifts.as_view(),
        name='user-lifts'),
    path('users/<int:pk>/<str:exercise>/',
        views.UserProfileExercise.as_view(),
        name='user-exercise'),
    path('lifts/', 
        views.LiftList.as_view(), 
        name='lift-list'),
    path('lifts/<int:pk>/',
        views.LiftDetail.as_view(), 
        name='lift-detail'),
])