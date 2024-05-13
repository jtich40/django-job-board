from django.forms import ModelForm
from .models import Job, Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . widgets import DatePickerInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['creator', 'updated', 'created']
        
        widgets = {
            # this will change the input type to date
            'deadline' : DatePickerInput(),
        }
        
class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['job', 'created']
    