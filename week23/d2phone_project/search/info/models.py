from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.name

class Phone(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()

    def __str__(self):
        return str(self.phone_number)

# Create your models here.
