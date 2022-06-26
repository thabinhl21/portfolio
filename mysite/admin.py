from django.contrib import admin
from .models import Project, Experience
# Register your models here.

#register Project model
admin.site.register(Project)

#register Experience model
admin.site.register(Experience)