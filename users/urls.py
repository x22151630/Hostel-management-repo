from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('', views.sign_up, name='sign_up'),
 
  
]