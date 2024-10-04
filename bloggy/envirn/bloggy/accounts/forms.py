from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserAuth

#signup validation class
class SignInForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    first_name = forms.CharField(required=True)
    username = forms.EmailField(required=True, min_length=3,max_length=15)
    password2=forms.CharField(required=True)
    password1=forms.CharField(required=True)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email=email.strip()
        return email

    class Meta:
        model = CustomUserAuth
        fields = ('username' , 'first_name' , 'phone_number' , 'password1')

