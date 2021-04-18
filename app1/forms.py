from .models import User,Admin
from django import forms





class login_form(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    dob = forms.DateField()
    phone = forms.IntegerField()
    password = forms.CharField(max_length=10)
    image = forms.FileField()
    mark = forms.IntegerField()