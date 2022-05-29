from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name