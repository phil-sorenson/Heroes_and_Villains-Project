from django.db import models

class SuperType(models.Model):
    type = models.CharField(max_length=255)
    
