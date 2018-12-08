from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Company(models.Model):
    """Model representing a company."""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length = 1000, blank=True)	
    emp_number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

class JobOffer(models.Model):
    """Model representing a job offer"""
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    deadline = models.DateField(blank=True)	
    salary = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length = 1000, blank=True)
    date_posted = models.DateField(default=timezone.now())	
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    apply_link = models.URLField(blank=True)
    @property
    def is_over(self):
        if self.deadline < timezone.now():
            return True
        return False

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length = 40, primary_key=True)

class JobTag(models.Model):
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
