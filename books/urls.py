from django.urls import path
from .views import list_of_books


urlpatterns = [
    path('index/', list_of_books, name='books'),
]
