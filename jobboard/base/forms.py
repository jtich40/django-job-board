from django.forms import ModelForm
from .models import Job
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . widgets import DatePickerInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['creator']
        
        widgets = {
            'deadline' : DatePickerInput(),
        }