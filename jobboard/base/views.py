from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

# Create your views here.

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
            form.save()
            # access url by name in urls.py
            return redirect('home')
        
    return render(request, 'base/job_form.html', {'form': form})