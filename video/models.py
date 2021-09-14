from django.db import models

# Create your models here.
class Chat(models.Model):
    room_name = models.CharField(max_length=255)
    allowed_users = models.CharField(max_length=255)
    total_users = models.CharField(max_length=255)
    no_of_users = models.CharField(max_length=255)
