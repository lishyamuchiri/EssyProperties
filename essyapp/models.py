from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name




class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    date = models.DateTimeField(max_length=50)
    location = models.CharField(max_length=100, default="Not specified")
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    location = models.CharField(max_length=100, default="Not specified")


    def __str__(self):
        return self.title
