from django.db import models


class Chat(models.Model):
    room_no = models.CharField(max_length=128)
    message = models.TextField()

    def __str__(self):
        return self.message
