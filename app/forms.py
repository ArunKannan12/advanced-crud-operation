from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter user name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter E-mail'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter password'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("An user with this email already exists!")
        return email

class empform(ModelForm):
    emp_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter employee name','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    emp_id=forms.CharField(max_length=6,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter employee id','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    phone=forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter employee phone number','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    class Meta:
        model=emp_details
        fields=['emp_name','emp_id','phone','e_position']
    def clean_emp_id(self):
        emp_id = self.cleaned_data["emp_id"]
        if emp_details.objects.filter(emp_id=emp_id).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("An user with this emp_id already exists!")
        return emp_id
    def clean_phone(self):
        phone= self.cleaned_data["phone"]
        if emp_details.objects.filter(phone=phone).exclude(pk=self.instance.pk).exists():
            raise ValidationError("An user with this phone number already exists!")
        return phone
    def __init__(self,*args, **kwargs):
        super(empform,self).__init__(*args, **kwargs)
        self.fields['e_position'].empty_label="select"
class positionform(forms.ModelForm):
    emp_position=forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter employee position','style':'width:300px;height:50px;border-radius:10px;border:2px skyblue solid;'}))
    class Meta:
        model=position
        fields=['emp_position']
    def clean_position(self):
        emp_position=self.cleaned_data["emp_position"]
        if position.objects.filter(emp_position=emp_position).exists():
            raise ValidationError("position already exist")
        return emp_position