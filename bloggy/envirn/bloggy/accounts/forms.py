from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUserAuth
from django.contrib.auth import authenticate

#signup validation class
class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    first_name = forms.CharField(required=True,min_length=3,max_length=15)
    email = forms.EmailField(required=True, min_length=3,max_length=40)
    password2 = forms.CharField(required=True)
    password1 = forms.CharField(required=True)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        email=email.strip()
        return email
        
    class Meta:
        model = CustomUserAuth
        fields = ('email' , 'first_name' , 'phone_number' , 'password1')
    
#signin validation class
class SignInForm(forms.Form):
    email=forms.CharField(required=True)
    password=forms.CharField(required=True)

    def clean(self) -> dict[str, Any]:
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')

        if email and password :
            user=authenticate(username=email,password=password)
            if not user :
                raise forms.ValidationError("invalid email or password")
        return super().clean()
        
