from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    # if the user is deleted, the job will remain in the database
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    location = models.CharField(max_length=200, null=True)
    deadline = models.DateTimeField(editable=True, null=True)
    
    def __str__(self):
        return self.title