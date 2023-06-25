from . import views
from django.urls import path
urlpatterns = [
     path('',views.loginpage,name="login"),
    path('signin/',views.signinpage,name="signin"),
    path('logout/',views.logoutpage,name="logout"),
    path("emp_form/",views.emp_form,name='emp_form'),
    path("emp_list/",views.emp_list,name='emp_list'),
    path("emp_update/<int:id>/",views.emp_update,name='emp_update'),
    path("emp_delete/<int:id>/",views.emp_delete,name='emp_delete'),
    path("emp_position/",views.emp_position,name='emp_position'),

]
