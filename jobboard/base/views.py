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