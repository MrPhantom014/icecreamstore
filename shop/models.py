from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    subject = models.TextField()
    date = models.DateField()

    def __str__(self):
        return (f"{self.fname} {self.lname}")