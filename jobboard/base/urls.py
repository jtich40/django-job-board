from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    
    path('', views.home, name="home"),
    # we are passing the primary key of the job to the job view which is the job id
    path('job/<str:pk>/', views.job, name="job"),
    path('create-job/', views.createJob, name="create-job"),
    path('update-job/<str:pk>', views.updateJob, name="update-job"),
    path('delete-job/<str:pk>', views.deleteJob, name="delete-job"),
    path('apply-job/<str:pk>', views.applyJob, name="apply-job"),
    path('success', views.success, name='success'),
    path('applicants/<str:pk>', views.applicantPage, name='applicants')
]
