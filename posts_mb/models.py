from django.db import models

# Create your models here.
class Posts(models.Model):
    text = models.TextField()

    def __str__(self):
        """Return First 50 Characters"""
        return self.text[:50]