from django.db import models
import datetime
from django.utils import timezone

class Blog(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=1)
