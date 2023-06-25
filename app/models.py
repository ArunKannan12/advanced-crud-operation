from django.db import models
from django.core.validators import RegexValidator
alpha=RegexValidator(r'^[a-zA-Z]{3,}','only alphabets are allowed and name should be more tha 3 charachets')
numbers=RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$','Enter a Valid Indian Phone Number')
pincode=RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$','Enter a valid employee id')

# Create your models here.
class position(models.Model):
    emp_position=models.CharField(max_length=50)
    def __str__(self):
        return self.emp_position
    
class emp_details(models.Model):
    emp_name=models.CharField( max_length=50,validators=[alpha])
    emp_id=models.CharField( max_length=10,validators=[pincode])
    phone=models.CharField( max_length=10,validators=[numbers])
    e_position=models.ForeignKey(position, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.emp_name
    