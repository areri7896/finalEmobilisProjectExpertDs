from django import forms
from django.forms import ModelForm
from .models import Profile, Location, Exam, Test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# create profile form
class ExamForm(forms.ModelForm):
    exam_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "first name", "class": "form-control"}), label="exam_name")
    exam_date = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "first date", "class": "form-control"}), label="exam_date")
    exam_time = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "first time", "class": "form-control"}), label="exam_time")
    exam_venue = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "first venue", "class": "form-control"}), label="exam_venue")

    class Meta:
        model = Exam
        fields = ('exam_name', 'exam_date', 'exam_time', 'exam_venue')


class TestForm(forms.ModelForm):
    test_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Test name", "class": "form-control"}), label="Test_name")
    test = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Test date", "class": "form-control"}), label="Test_date")
    test_time = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Test time", "class": "form-control"}), label="Test_time")
    test_venue = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Test venue", "class": "form-control"}), label="Test_venue")

    class Meta:
        model = Test
        fields = ('test_name', 'test_date', 'test_time', 'test_venue')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('id_no', 'email', 'phone_number', 'gender')

        # widgets


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control '
        self.fields['username'].widget.attrs['placeholder'] = 'Student No/ Employee No'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
