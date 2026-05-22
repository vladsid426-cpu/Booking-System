from django.db import models

# Create your models here.
class RoomCategory(models.Model):
    choice = [('standart','стандарт'),('premium','преміум'),('presidental','люкс')]
    category = models.CharField()
    class meta():
        verbose_name = 'Категорія кімнати'
class Room(models.Model):
    name = models.CharField()
    room_category = models.ForeignKey(RoomCategory,on_delete=models.CASCADE)
    class meta():
        verbose_name = 'Назви кімнат'
class Booking(models.Model):
    start_data = models.DateTimeField(null=False)
    end_data = models.DateTimeField(null=False)

    room = models.ForeignKey(Room,on_delete=models.CASCADE)

    class meta():
        verbose_name = 'Замовлення'
    def __str__(self):
        return f"Замовлення {self.room.name} ({self.start_date.strftime('%Y-%m-%d')})"