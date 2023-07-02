from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
