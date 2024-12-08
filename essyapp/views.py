from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from essyapp.forms import BookingForm, ImageUploadForm
from essyapp.models import Contact, Booking, User,ImageModel
from essyapp.forms import BookingForm


# Create your views here.
def starter(request):
    return render(request,'starter-page.html')


def index(request):
    return render(request,'index.html')
@login_required
def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def login(request):
    return render(request,'login.html')

def properties(request):
    return render(request,'properties.html')

@login_required
def view(request):
    return render(request,'view.html')


def contact (request):
    if request.method == "POST":
        mycontacts=Contact (
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message'],

        )
        mycontacts.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')

def book(request):
    if request.method == "POST":
        myappointments=Booking(

                name = request.POST['name'],
                email = request.POST['email'],
                phone = request.POST['phone'],
                date = request.POST['date'],
                location = request.POST['location'],
                message = request.POST['message'],

        )
        myappointments.save()
        return redirect('/book')
    else:
        return render(request,'book.html')


def delete_contact(request, id):
    appoint = Contact.objects.get(id=id)
    appoint.delete()
    return redirect('/cshow')

def delete_booking(request, id):
    appoint = Booking.objects.get(id=id)
    appoint.delete()
    return redirect('/bookshow')


def edit(request, id):
    editbooking = Booking.objects.get(id=id)
    return render(request, 'edit.html', {'book': editbooking})





def update(request, id):
    # Retrieve the booking object or return a 404 if not found
    updateinfo = Booking.objects.get( id=id)
    if request.method == "POST":
      form = BookingForm(request.POST, instance=updateinfo)
      if form.is_valid():
       form.save()
       return redirect('/bookshow')


      else:
         return render (request,'edit.html')

    else:
        form = BookingForm(instance=updateinfo)

    return render(request, 'edit.html')




def cshow (request):
    allcontacts=Contact.objects.all()
    return render(request,'cshow.html', {'contact':allcontacts})


def bookshow (request):
    allbookings=Booking.objects.all()
    return render(request,'bookshow.html', {'book':allbookings})



def view(request):
    if request.method == 'POST':
        if User.objects.filter(
                name=request.POST['name'],
                password = request.POST['password'] ).exists():
                       return render(request,'view.html')

        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def bookshow(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if User.objects.filter(name=name, password=password).exists():
            request.session['name'] = name  # Store username in session
            # Redirect to the page the user intended to access
            next_page = request.POST.get('next', 'bookshow')  # Default to bookshow
            return redirect(next_page)
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')




def uploadimage(request):
    if request.method=='POST':
        if User.objects.filter(
                name=request.POST['name'],
                password=request.POST['password'] ).exists():
             user = User.objects.get(
                 name=request.POST['name'],
                 password=request.POST['password'])
             return render(request,'upload.html',{'users':user})
        else:
             return render(request,'login.html')
    else:
        return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        if User.objects.filter(name=name, password=password).exists():
            request.session['name'] = name  # Store username in session
            # Redirect to the page the user intended to access
            next_page = request.POST.get('next', 'bookshow')  # Default to bookshow
            return redirect(next_page)
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')