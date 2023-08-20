from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name