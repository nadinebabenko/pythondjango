from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.utils.translation import gettext as _

# Create your models here.
class User(AbstractUser):
    amount_of_money = models.IntegerField(default=1000)
    points = models.IntegerField(default=0)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='cards_users_permissions',
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='cards_users_groups',
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=_('groups'),
    )


class Card(models.Model):
    name_character = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    image_url = models.URLField()
    date_of_birth = models.DateField(null=True)
    patronus = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    xp_points = models.IntegerField(default=0)
    current_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cards_owned')
    previous_owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cards_sold')

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = random.randint(200, 2000)
        if not self.xp_points:
            self.xp_points = random.randint(1, 10)
        super().save(*args, **kwargs)