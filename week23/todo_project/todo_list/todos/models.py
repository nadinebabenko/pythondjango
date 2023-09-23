from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(default=timezone.now)
    date_completion = models.DateTimeField(null=True, blank=True)
    deadline_date = models.DateTimeField(null=True, blank=True)