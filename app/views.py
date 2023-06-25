from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def signinpage(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,user + ",your registration is successfull 🤩 ")
            return redirect('login')
    context={
        'form':form
        }
    return render (request,'signup.html',context)
def loginpage(request):
   if request.user.is_authenticated:
    return redirect('emp_form')
   else:
    if request.method == 'POST':
        uname=request.POST.get('username').lower()
        pass1=request.POST.get('password')
        user=authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successfull ,"+str(user))
            return redirect('emp_form')
        else:
            messages.info(request,"Please check the username and password 😐")
            return redirect('login')
    return render (request,'loginpage.html')
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"you have been successfully logged out from this page 😊 ")
        return redirect('login')
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
def emp_position(request):
    form=positionform()
    if request.method == 'POST':
        form=positionform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"employee position added successfully")
    context={
        'form':form,
    }
    return render (request,'position.html',context)
