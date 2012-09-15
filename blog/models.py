from django.db import models

class Blog(models.model):
    name = models.CharField(max_length=200)

class Post(models.model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField()
