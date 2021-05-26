from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloAPI.as_view(), name='Index')
]
