from django import forms
from django.forms import ModelForm
from .models import Profile, Location


# create profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('id_number', 'email', 'phone_number', 'gender')

        # widgets
