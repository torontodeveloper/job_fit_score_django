from django.db import models
from django.views.generic.list import ListView


# Create your models here.

class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    cv_file = models.FileField()
    
    class Meta:
        db_table = "candidate"
        
    def save(self):
        super().save()