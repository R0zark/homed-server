from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=60)
    extension = models.CharField(max_length=60)
    capacity = models.IntegerField()
    url = models.FileField()

    def __str__(self):
        return f"name: {self.name}, extension: {self.extension},capacity: {self.capacity}, url: {self.url}" 