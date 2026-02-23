from rest_framework import serializers
from .models import Concert, Booking


class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'
        read_only_fields = ['available_tickets']


class BookingSerializer(serializers.ModelSerializer):
    concert_details = ConcertSerializer(source='concert', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'concert', 'concert_details', 'tickets_booked']