from django import forms
from .models import Student,Teacher

class AddForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','department','email','username','password','gender','image')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),

        }

class TeacherReg(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','department','username','password')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

class TeacherLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)