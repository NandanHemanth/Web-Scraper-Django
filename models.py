from django.db import models
from django.contrib import admin
from .models import Candidate

admin.site.register(Candidate)
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.FloatField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
