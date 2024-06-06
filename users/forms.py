from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from cloudinary.forms import CloudinaryFileField

class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 



class UserUpdateForm(forms.ModelForm) :
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm) :
    image = CloudinaryFileField()

    class Meta:
        model = Profile
        # fields = ['image']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].options={
            'tags': 'new_image',
        }
    

