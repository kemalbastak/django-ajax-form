from django.db import models

# Create your models here.
class UserEntry(models.Model):
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    link = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    image = models.ImageField(upload_to='photos/uploaded_images', blank = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.header}"

class Language(models.Model):
    language = models.CharField(max_length=20)
    shortcut = models.CharField(max_length=5)
    flag = models.ImageField(upload_to='photos/uploaded_images', blank = True)

    def __str__(self) -> str:
        return f"{self.language}"