from django.shortcuts import render
from .models import Project, Experience
# Create your views here.

# create view for projects page
def projects(request):
    title = "Projects"
    # query that gets all Project objects from database
    qs = Project.objects.all()
    template = "projects.html"
    context = {
        "title": title,
        "project_list": qs,
    }
    return render(request, template, context)

# create view for experience page
def experience(request):
    title = "Experience"
    qs = Experience.objects.all()
    template = "experience.html"
    context = {
        "title": title,
        "work_list": qs,
    }
    return render(request, template, context)