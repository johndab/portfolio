from django.db import models
from django.utils import timezone

class CvRow(models.Model):
    section = models.CharField(max_length=100)
    date = models.CharField(max_length=100, default="", blank=True)
    subtitle = models.TextField(default="", blank=True)
    title = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title