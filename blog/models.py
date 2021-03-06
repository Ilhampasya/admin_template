from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    contents = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title