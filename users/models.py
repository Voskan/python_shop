from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=70)
    dob = models.DateField()
    phone = models.CharField(max_length=12)
    card_number = models.IntegerField()
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/users/%Y/%m/%d')
