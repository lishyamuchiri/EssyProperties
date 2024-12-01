from django.shortcuts import render

# Create your views here.
def starter(request):
    return render(request,'starter-page.html')
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def properties(request):
    return render(request,'properties.html')

def contact(request):
    return render(request,'contact.html')

def book(request):
    return render(request,'book.html')