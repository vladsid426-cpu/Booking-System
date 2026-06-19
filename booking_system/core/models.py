from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class RoomCategory(models.Model):
    choice = [
        ('standart','стандарт'),
        ('premium','преміум'),
        ('presidental','люкс')
    ]
    name = models.CharField()
    is_active = models.BooleanField(default=True,null=True)
    
    class Meta:
        verbose_name = 'категорія кімнат'
        verbose_name_plural = 'категорія кімнат'

    
    def __str__(self):
        return f'{self.name}'

    

class Room(models.Model):
    number = models.IntegerField(unique=True)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Назви кімнат'
        verbose_name_plural = 'назви кімнат'

    def __str__(self):
        return f'{self.number} - {self.room_category}'
class BookingStatus(models.TextChoices):
    PENDING = "pending", "Очікує"
    CONFIRMED = "confirmed", "Підтверджено"
    CANCELED = "canceled", "Скасовано"    
    class Meta:
        verbose_name = 'Статус замовлень'
        verbose_name_plural = 'Статус Замовлень'

class Booking(models.Model):
    
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    status = models.CharField(choices=BookingStatus.choices)
    created_at = models.DateTimeField(null=True)
    comment = models.TextField(null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='room',verbose_name='кімната')
    user = models.ForeignKey( 
        User, on_delete=models.PROTECT, related_name="bookings", verbose_name="Користувач"
    )



    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
    
    def __str__(self):
        return f"Замовлення {self.created_at} ({self.status})"
    
