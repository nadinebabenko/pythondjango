from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from imageshare.models import Image, Profile


@receiver(post_save, sender=Image)
def update_profile(sender, instance, created, **kwargs):
    if created:
        
        user = instance.user
         
        profile = Profile.objects.get(user=user)
         
        profile.num_images += 1
        
        profile.save()