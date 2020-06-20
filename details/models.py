import datetime

from django.db import models
from django.utils import timezone


class Project(models.Model):
    project_name = models.CharField(unique=True, max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='details/static/details/assets', blank=True, null=True)
    link = models.URLField(max_length=150, blank=True, null=True)
    start_date = models.DateField('date started')
    end_date = models.DateField(name='date ended', blank=True, null=True)

    def __str__(self):
        """returns a string representation of the object model"""
        return self.project_name

