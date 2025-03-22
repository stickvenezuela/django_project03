from django.urls import path

from .views import MoviesView

path = [
    path('', MoviesView.as_view(), name='movies')
]