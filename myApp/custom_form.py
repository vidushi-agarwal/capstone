from django import forms#(here we have to inherit ModelForm from forms like in models Model)
from .models import Profile

class RegisterDp(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp']
