from django.db import models
from datetime import date
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    """Base user model extension"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ALL_STATUS = (
        (0, 'Closed to offers'),
        (1, 'Open to offers'),
        (2, 'Actively interviewing'),
        (3, 'Starting to look'))
    status = models.IntegerField(default=1,choices = ALL_STATUS)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '+123456789'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    is_recruiter = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Company(models.Model):
    """Model representing a company."""
    name = models.CharField(max_length=200)
    description = models.TextField(max_length = 1000, blank=True)	
    emp_number = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    """Model representing user->company subscription"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class JobOffer(models.Model):
    """Model representing a job offer"""
    name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    deadline = models.DateField(blank=True)	
    salary = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length = 1000, blank=True)
    date_posted = models.DateField(auto_now_add=True)	
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    apply_link = models.URLField(blank=True)
   
    @property
    def is_over(self):
        if self.deadline < timezone.now():
            return True
        return False
    
    def __str__(self):
        return self.name

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    
class Tag(models.Model):
    name = models.CharField(max_length = 40, primary_key=True)

    def __str__(self):
        return self.name

class JobTag(models.Model):
    job = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
