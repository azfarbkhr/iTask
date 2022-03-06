from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('itask/resumes/<file_name>', views.resumes, name='resume'),
]
