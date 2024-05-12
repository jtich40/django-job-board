from django.forms import ModelForm
from .models import Job
from django.contrib.auth.models import User
from . widgets import DatePickerInput


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['creator']
        
        widgets = {
            'deadline' : DatePickerInput(),
        }