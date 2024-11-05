from django.contrib import admin
from django.urls import path
from .views import index , result , vote ,yes
urlpatterns = [
    path('', index),
    path('result/<int:il>',result,name="result"),
    path('vote/<int:val>',vote,name="vote"),
    path('yes',yes,name="yes")
]
