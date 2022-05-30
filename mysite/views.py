from django.shortcuts import render
from .models import Project
# Create your views here.

# create view for projects page
def projects(request):
    title = "Projects"
    # query that gets all Project objects from database
    qs = Project.objects.all()
    template = "projects.html"
    context = {
        "title":title,
        "project_list": qs,
    }
    return render(request, template, context)