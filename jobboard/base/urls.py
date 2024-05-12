from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # we are passing the primary key of the job to the job view which is the job id
    path('job/<str:pk>/', views.job, name="job"),
    path('create-job/', views.createJob, name="create-job")
]
