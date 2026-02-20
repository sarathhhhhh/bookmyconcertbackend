from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Concert(models.Model):
    name = models.CharField(max_length=30)
    date_time=models.DateTimeField()
    venue=models.CharField(max_length=100)
    ticket_price=models.DecimalField(max_digits=8,decimal_places=2)
    available_tickets=models.PositiveIntegerField()

class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    concert=models.ForeignKey(Concert,on_delete=models.CASCADE)
    tickets_booked=models.PositiveIntegerField()
    
    class Meta:
        unique_together = ('user', 'concert')




    

