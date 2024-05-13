from django.shortcuts import render, redirect
from .models import Job
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import JobForm, RegisterForm, ApplicationForm

# Create your views here.

# don't use login as function name because it's a built-in function we are using
def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        # make sure the email is lowercase
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")
        # this will authenticate the user by checking email and password
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password is incorrect.")
    
    return render(request, 'base/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page = 'register'
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # we need to save the user first before we can authenticate them
            user = form.save(commit=False)
            # clean the data so that the email is lowercase
            user.email = user.email.lower()
            user.save()
            # login the user after they have registered
            login(request, user)
            return redirect('home')
    
    return render(request, 'base/login_register.html', {'form': form})

def home(request):
    jobs = Job.objects.all()
    # this will render the home.html template and pass the jobs to the template
    return render(request, 'base/home.html', {'jobs': jobs})

def job(request, pk):
    # find by job id
    job = Job.objects.get(id=pk)
    
    return render(request, 'base/job.html', {'job': job})

def createJob(request):
    form = JobForm()
    if request.method == 'POST':
        # take the data from the form and create a new job
        form = JobForm(request.POST)
        if form.is_valid():
            job =form.save(commit=False)
            # set the creator of the job to the current user
            job.creator = request.user 
            job.save()
            # access url by name in urls.py
            return redirect('home')
        
    return render(request, 'base/job_form.html', {'form': form})

def updateJob(request, pk):
    job = Job.objects.get(id=pk)
    # this will prefill the form with the job data
    form = JobForm(instance=job)
    
    if request.method == 'POST':
        # this will update the job with the new data
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            # pass the job id to the job view so user can see the updated job
            return redirect('job', pk=job.id)
        
    return render(request, 'base/job_form.html', {'form': form})

def deleteJob(request, pk):
    job = Job.objects.get(id=pk)
    
    if request.method == "POST":
        job.delete()
        return redirect('home')
    
    return render(request, 'base/delete_job.html', {'job': job})

def applyJob(request, pk):
    # we need to get the job so we can send the email to the contact email
    job = Job.objects.get(id=pk)
    form = ApplicationForm()
    
    if request.method == 'POST':
        # we are passing the data including the files to the form
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # create the job application but don't save yet
           application = form.save(commit=False)
           application.job = job
           application.save()
            
        return redirect('success')
    
    return render(request, 'base/application_form.html', {'form': form})

def success(request):
    return render(request, 'base/success.html')
        