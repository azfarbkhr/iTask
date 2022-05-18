from urllib.parse import urlparse
from django.urls import URLPattern, path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('population-chart/', views.population_chart, name='population-chart')
]