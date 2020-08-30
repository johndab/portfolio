from django.db import models
from django.utils import timezone

class CvRow(models.Model):
    section = models.CharField(max_length=200)
    title = models.TextField()
    subtitle = models.TextField()
    date = models.TextField()
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title