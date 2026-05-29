from django.db import models
from django.core.validators import MaxValueValidator

class RoomCategory(models.Model):
    choice = [
        ('standart','стандарт'),
        ('premium','преміум'),
        ('presidental','люкс')
    ]
    category = models.CharField()
    
    class Meta:
        verbose_name = 'Категорія кімнати'
    
    def str(self):
        return f'{self.category}'
    

class Room(models.Model):
    name = models.CharField()
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Назви кімнат'

    def str(self):
        return f'{self.name,self.room_category}'
    

class Booking(models.Model):
    start_data = models.DateTimeField(null=False)
    end_data = models.DateTimeField(null=False)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Замовлення'
    
    def str(self):
        return f"Замовлення {self.room.name} ({self.start_data.strftime('%Y-%m-%d')})"

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