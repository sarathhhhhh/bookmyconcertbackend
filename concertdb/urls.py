from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ConcertViewSet,BookTicketView,MyBookingsView

router= DefaultRouter()
router.register(r'concerts',ConcertViewSet,basename='concert')

urlpatterns = [
    path('',include(router.urls)),
    path('book/',BookTicketView.as_view(),name='book-ticket'),
    path('my-bookings/',MyBookingsView.as_view(),name='my-bookings')
    ]

