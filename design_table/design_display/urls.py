from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('change',views.change),
    path('post', views.post),
]