from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#user model
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    interests = models.ManyToManyField('Interest', blank=True)

    def __str__(self):
        return self.username

#Interest model
class Interest(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

#Event model
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    location = models.CharField(max_length=100)
    date = models.DateTimeField()
    interests = models.ManyToManyField(Interest, related_name='events')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#Notification model
class Notification(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name='Notification')
    messege =models.TextField()
    is_read =models.BooleanField(default=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:30]}"