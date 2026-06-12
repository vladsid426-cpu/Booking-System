from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Review(models.Model):
    username = models.CharField()
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)],null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta():
        verbose_name = 'відгуки'
        verbose_name_plural = 'відгуки'
    def __str__(self):
        return f"{self.username}:{self.text}|{self.created_at}"
    
class Booking(models.Model):
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    created_at = models.DateTimeField(null=True)
    comment = models.TextField(null=True)


    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
    
    def __str__(self):
        return f"Замовлення {self.room.name} ({self.start_date.strftime('%Y-%m-%d')})"