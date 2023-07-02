from . import views
from django.urls import path
urlpatterns = [
   
    path("",views.emp_form,name='emp_form'),
    path("emp_list/",views.emp_list,name='emp_list'),
    path("emp_update/<int:id>/",views.emp_update,name='emp_update'),
    path("emp_delete/<int:id>/",views.emp_delete,name='emp_delete'),
  

]
