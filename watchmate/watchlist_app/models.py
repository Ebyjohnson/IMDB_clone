from django.db import models

class Movie(models.Model):
    Name = models.CharField(max_length=50)
    About  = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name