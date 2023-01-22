from django.urls import path

from .views import TrelloCardAPI

app_name = 'api_v1'
urlpatterns = [
    path('trello_cards/', TrelloCardAPI.as_view()),
]
