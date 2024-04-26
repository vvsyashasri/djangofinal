from django.urls import path
from .import views

urlpatterns = [
   path('adminhome',views.adminhome,name="adminhome"),
   path('adminlogout',views.logout,name="adminlogout"),
   path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
   path("viewstudents",views.viewstudents,name="viewstudents"),
   path("viewcourses",views.viewcourses,name="viewcourses"),
   path("success",views.success,name="success"),
   path("viewfaculty",views.viewfaculty,name="viewfaculty"),
   path("adminstudent",views.adminstudent,name="adminstudent"),
   path("adminfaculty",views.adminfaculty,name="adminfaculty"),
   path("admincourse",views.admincourse,name="admincourse"),

]
