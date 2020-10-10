from django.urls import path
from asteroids import views

urlpatterns = [
    path('', views.index),
    path('/asteroids_list', views.asteroids_list)
]
