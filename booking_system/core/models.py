from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.decorators import login_required


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

    
@login_required
class Room(models.Model):
    number = models.IntegerField(unique=True)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)



    class Meta:
        verbose_name = 'Назви кімнат'
        verbose_name_plural = 'назви кімнат'

    def __str__(self):
        return f'{self.number} - {self.room_category}'
    
@login_required
class Booking(models.Model):
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    created_at = models.DateTimeField(null=True)
    comment = models.TextField(null=True)


    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
    
    def __str__(self):
        return f"Замовлення {self.room.name} ({self.start_date.strftime('%Y-%m-%d')})"

@login_required  
class Review(models.Model):
    guest_name = models.CharField()
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return f"{self.guest_name}-{self.text}"
    class Meta:
            verbose_name = 'Коментарі'
            verbose_name_plural = 'Коментарі'
