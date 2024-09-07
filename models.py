from django.db import models

# Create your models here.
class BookModel(models.Model):
    Name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    read_by=models.CharField(max_length=50)