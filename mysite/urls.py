from django.urls import path
from website.views import about
from .views import projects

app_name = "mysite"

urlpatterns = [
    path('', about, name=''),
    path('projects/', projects, name='projects'),
]