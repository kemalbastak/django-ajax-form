from django.db import models
import uuid


# Create your models here.
class UserEntry(models.Model):
    uuid = models.CharField(max_length=50)
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    image = models.ImageField(blank = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.header}"