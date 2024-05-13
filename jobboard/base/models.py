from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Job(models.Model):
    # if the user is deleted, the job will remain in the database
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True)
    deadline = models.DateField(editable=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    resume = models.FileField(null=True)
    cover_letter = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.job.title}'