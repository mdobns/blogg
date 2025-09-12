from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField( max_length=50)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name