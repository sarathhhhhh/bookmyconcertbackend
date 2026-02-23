from django.urls import path
from .views import ConcertListView, ConcertDetailView


urlpatterns = [
    path('concerts/',ConcertListView.as_view(),name='concert-list'),
    path('concerts/<int:pk>/',ConcertDetailView.as_view(),name='concert-details'),
    ]

