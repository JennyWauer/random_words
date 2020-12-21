from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_word),
    path('generate/', views.generate),
    path('reset/', views.reset),
]