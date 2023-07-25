from django.contrib.auth.models import AbstractUser # pylint: disable=C0415
from django.db import models # pylint: disable=C0415

# Create your models here.
class ApiUser(AbstractUser):
    """abstract class"""
    pass


class Hotel(models.Model):
    """class Hotel"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Room(models.Model):
    """class Room"""
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hotel.name}. Room num: {self.num}'


class Booking(models.Model):
    """class Booking"""
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='bookings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}; {self.room.hotel.name}; {self.room.num}'
        
