from django.db import models

# Create your models here.


class BlogEntry(models.Model):
    title = models.CharField(max_length=160)
    body = models.TextField()
