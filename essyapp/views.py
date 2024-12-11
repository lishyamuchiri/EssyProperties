from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from essyapp.forms import BookingForm, ImageUploadForm
from essyapp.models import Contact, Booking, ImageModel,User


# Create your views here.
def index(request):
    if request.method == 'POST':
        if User.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']).exists():
            return render(request, 'index.html')

        else:
            return render(request, 'accounts/login.html')

    else:
        return render(request, 'accounts/login.html')

@login_required
def starter(request):
    return render(request, 'starter-page.html')


def login(request):
    return render(request,'accounts/login.html')


@login_required
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')




def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Check if passwords match
        if password != password_confirm:
            return HttpResponse("Passwords do not match. Please try again.", status=400)

        # Create the user if passwords match
        if  username and password:  # Ensure all fields are filled
            members = User(
                username=username,
                password=password,
            )
            members.save()
            return redirect('/login')
        else:
            return HttpResponse("All fields are required.", status=400)
    else:
        return render(request, 'accounts/register.html')



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})





def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})


def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('showimage')


def bookshow(request):
    allbookings = Booking.objects.all()
    return render(request, 'bookshow.html', {'book': allbookings})


@login_required
def cshow(request):
    allcontacts = Contact.objects.all()
    return render(request, 'cshow.html', {'contact': allcontacts})


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})


def contact(request):
    if request.method == "POST":
        mycontacts = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontacts.save()
        return redirect('/contact')
    else:
        return render(request, 'contact.html')


def edit(request, id):
    editbooking = Booking.objects.get(id=id)
    return render(request, 'edit.html', {'book': editbooking})


def update(request, id):
    updateinfo = Booking.objects.get(id=id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=updateinfo)
        if form.is_valid():
            form.save()
            return redirect('/bookshow')
    else:
        form = BookingForm(instance=updateinfo)
    return render(request, 'edit.html', {'form': form})


def delete_booking(request, id):
    appoint = Booking.objects.get(id=id)
    appoint.delete()
    return redirect('/bookshow')


def delete_contact(request, id):
    appoint = Contact.objects.get(id=id)
    appoint.delete()
    return redirect('/cshow')

def  properties(request):
    return render(request, 'properties.html')












