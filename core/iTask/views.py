from django.shortcuts import redirect, render
from django.http import HttpResponse
import os
from django.http import FileResponse
import requests
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        response = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
        return HttpResponse(response.json()['joke'] + '<br><br>' + '<a href="/admin">iTask Admin</a>')
    else:
        return redirect('admin:login')

def resumes(request, file_name):
    file_path = os.path.join(os.path.dirname(__file__), 'resumes',  file_name)
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')