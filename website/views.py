from django.shortcuts import render
from .forms import ContactForm


# create view for about page, which is also the home page
def about(request):
    title = "Binh Le"
    heading = "Hi, my name is Binh!"
    content = "I'm an aspiring software developer"
    template = "about.html"
    # context dictionary to send info to about.html template
    context = {
        "title":title, 
        "heading":heading, 
        "content":content
    }
    return render(request, template, context)

# create view for contact page
def contact(request):
    title = "Contact"
    template = "contact.html"
    form = ContactForm(request.POST or None) # if the data is not empty, move onto form validation
    # built in Django form validation
    if form.is_valid():
        print(form.cleaned_data) # prints a dictionary of validated form input fields and their values
        form = ContactForm() # refresh filled contact form back to empty
    context = {
        "title":title,
        "form":form
    }
    return render(request, template, context)
