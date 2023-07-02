from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.

def emp_form(request):
    form=empform()
    if request.method == 'POST':
        form=empform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"employee added successfully")
            return redirect('emp_form')
    
    if 'q' in request.GET:
        q=request.GET['q']
        emp_list=emp_details.objects.filter(Q(emp_name__icontains=q)|Q(emp_id__icontains=q)|Q(phone__icontains=q))
    else:
        emp_list=emp_details.objects.all()
   
    context={
        'form':form,
        'emp_list':emp_list,
       
    }
    return render(request,'emp_form.html',context)
def emp_list(request):
    pass

def emp_update(request,id):
    update_emp=emp_details.objects.get(id=id)
    form=empform(instance=update_emp)
    if request.method == 'POST':
        form=empform(request.POST,instance=update_emp)
        if form.is_valid():
            form.save()
            messages.success(request,"updae successfull")
            return redirect('emp_form')
        else:
            form=empform(request.POST,instance=update_emp)
    context={
        'update_emp':update_emp,
        'form':form
    }
    return render(request,'emp_update.html',context)

def emp_delete(request,id):
    delete=emp_details.objects.get(id=id)
    name=emp_details.objects.all()
    if request.method == 'POST':
        messages.warning(request,"employee detail deleted successfully")
        delete.delete()
        return redirect('emp_form')
    context={
        'delete':delete
    }
    return render(request,'emp_delete.html')
