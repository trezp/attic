from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50, default="This is a title")
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
