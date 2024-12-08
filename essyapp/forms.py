from django import forms
from essyapp.models import Booking, ImageModel


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

