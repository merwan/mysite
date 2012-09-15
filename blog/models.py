from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField()
