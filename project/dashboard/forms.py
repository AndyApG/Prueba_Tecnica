from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(AuthenticationForm):

    
    password = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user = authenticate(username=email, password=password)
            if self.user is None:
                raise forms.ValidationError('Correo electrónico o contraseña incorrectos.')

        return self.cleaned_data

    def get_user(self):
        return self.user
    


class UserForm(UserCreationForm):


    email = forms.EmailField(required=True)

    class Meta:


        model = User
        fields = ['email', 
                  'password1', 
                  'password2'] 

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  
        if commit:
            user.save()
        return user



class LoadForm(forms.Form):
    file = forms.FileInput()

   

    
