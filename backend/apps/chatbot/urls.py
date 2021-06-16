from django.urls import path

from .api import api_chatbot


urlpatterns = [
    path('api/v1/chatbot/', api_chatbot)
]