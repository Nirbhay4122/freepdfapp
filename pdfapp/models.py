from statistics import mode
from django.db import models

# Create your models here.


class pdfinfo(models.Model):
    year = models.IntegerField(max_length=4)
    section = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    file = models.FileField(blank=True, null=True)
    dou = models.DateField(auto_now_add=True)
    college = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title
