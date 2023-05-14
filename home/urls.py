from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getAllJobs', views.getAllJobs, name='getAllJobs'),
    path('get/<int:id>', views.get, name='get'),
    path('getRelevantJobs', views.getRelevantJobs, name='getRelevantJobs'),
    path('search', views.search, name='search'),
]

