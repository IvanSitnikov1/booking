from django.contrib.auth.models import AbstractUser # pylint: disable=E0401
from django.db import models # pylint: disable=E0401

# Create your models here.
class ApiUser(AbstractUser):# pylint: disable=R0903
    """abstract class"""
    pass # pylint: disable=E0401


class Hotel(models.Model):# pylint: disable=R0903
    """class Hotel"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Room(models.Model):# pylint: disable=R0903
    """class Room"""
    num = models.PositiveIntegerField()
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hotel.name}. Room num: {self.num}'


class Booking(models.Model):# pylint: disable=R0903
    """class Booking"""
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name='bookings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}; {self.room.hotel.name}; {self.room.num}'
