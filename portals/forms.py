from django import forms
from django.forms import ModelForm
from .models import Profile, Address


# create profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('surname', 'firstname', 'other_names', 'id_number', 'email', 'phone_number', 'gender')
