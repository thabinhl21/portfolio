from django.shortcuts import render

# create view for about page, which is also the home page
def about(request):
    return render(request, "about.html", {})