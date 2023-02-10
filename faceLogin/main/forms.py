from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import student1


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo = forms.ImageField(help_text="upload clear profile picture", required=False)
    class Meta:
        model = User
        fields = ("username", "email", "password1")
        
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
                user.save()
        return user
    

class studentForm(forms.ModelForm):
    # file = forms.ImageField(allow_empty_file=False,required=True)
    class Meta:
        model = student1
        fields = "__all__"
