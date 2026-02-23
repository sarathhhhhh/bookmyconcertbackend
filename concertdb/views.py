from django.shortcuts import render
from .serializers import ConcertSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import status
from .models import Concert,Booking



class ConcertListView(generics.ListAPIView):
    queryset=Concert.objects.all()
    serializer_class=ConcertSerializer
    permission_classes=[AllowAny]

class ConcertDetailView(generics.RetrieveAPIView):
    queryset=Concert.objects.all()
    serializer_class=ConcertSerializer
    permission_classes=[AllowAny]


class BookTicketView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        concert_id = request.data.get('concert')
        tickets_requested = request.data.get("tickets_booked")

        if not concert_id or not tickets_requested:
            return Response(
                {"error":"Concert and ticket count required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if int(tickets_requested)<=0:
            return Response(
                {"error":"Ticket count must be greater than 0."},
                status=status.HTTP_400_BAD_REQUEST
            )
        concert = get_object_or_404(Concert,id=concert_id)

        with transaction.atomic():
            booking=Booking.objects.filter(
                user=request.user,
                concert=concert
            ).first()

            existing_tickets=booking.tickets_booked if booking else 0
            total_tickets=existing_tickets+int(tickets_requested)

            if total_tickets>3:
                return Response(
                    {"error":"Maximum 3 tickets allowed per concert."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            concert.available_tickets -= int(tickets_requested)
            concert.save()

            


