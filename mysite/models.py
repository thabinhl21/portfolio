from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)    # a unique URL for each project
    tools = models.CharField(max_length=250)

    def get_absolute_url(self):
        return f"/projects/{self.slug}"

