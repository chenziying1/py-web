from django.db import models

# weather_crawler_app/models.py

from django.db import models

class CrawlerTask(models.Model):
    enabled = models.BooleanField(default=True)
    running_time = models.TimeField()
    last_run = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Not started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Crawler Task - {self.id}"

