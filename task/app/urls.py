from django.urls import path, include
from task.app import views

urlpatterns = [
    path('', views.index),
    path("post/user/", views.create_user),
]