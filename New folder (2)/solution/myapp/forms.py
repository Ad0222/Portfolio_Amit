from django import forms
from .models import MyModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['image']

# from django import forms
# from .models import MyModel
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ['image']



