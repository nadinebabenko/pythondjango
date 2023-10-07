from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_images_uploaded = models.IntegerField(default=0)