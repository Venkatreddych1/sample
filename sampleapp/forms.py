from django import forms
from .models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        widgets = {'pwd': forms.PasswordInput(),}
        fields = ['email','user', 'pwd','fname','lname','date']
class LoginForm(forms.Form):
    email = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())


