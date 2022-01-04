"""HospitalManagement URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HMS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('facultyappointment', views.faculty_appointment, name='facultyappointment'),
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('pharmacistlogin/',views.pharmacistlogin,name='pharmacistlogin'),
    path('doctordashboard/',views.doctordashboard,name='doctordashboard'),
    path('pharmacistdashboard/',views.pharmacistdashboard,name='pharmacistdashboard'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('doctoreditprofile/',views.doctoreditprofile,name='doctoreditprofile'),
    path('doctorschedule/',views.doctorschedule,name='doctorschedule'),
    path('pharmacistschedule/',views.pharmacistschedule,name='pharmacistschedule'),
    path('pharmacisteditprofile/',views.pharmacisteditprofile,name='pharmacisteditprofile'),
    path('addmedicines/',views.addmedicines,name='addmedicines'),
    path('studentsappointments/',views.studentsappointments,name='studentsappointments'),
    path('facultyappointments/',views.facultyappointments,name='facultyappointments'),
    path('facultymedicines/',views.facultymedicines,name='facultymedicines'),
    path('studentsmedicines/',views.studentsmedicines,name='studentsmedicines'),
    path('addmedicinesforstudent/<int:tid>',views.addmedicinesforstudent,name='addmedicinesforstudent'),
    path('addmedicinesforfaculty/<int:tid>',views.addmedicinesforfaculty,name='addmedicinesforfaculty'),
    path('showmedicinesforstudent/<int:tid>', views.showmedicinesforstudent, name='showmedicinesforstudent'),
    path('showmedicinesforfaculty/<int:tid>', views.showmedicinesforfaculty, name='showmedicinesforfaculty'),
    path('completestudenttreatment/<int:tid>', views.completestudenttreatment, name='completestudenttreatment'),
    path('completefacultytreatment/<int:tid>', views.completefacultytreatment, name='completefacultytreatment'),
    path('otppassword/',views.otppassword,name='otppassword'),
    path('passwordreset/',views.passwordreset,name='passwordreset'),
    path('completlytreatedStudents/',views.completlytreatedStudents,name='completlytreatedStudents'),
    path('completlytreatedFaculty/',views.completlytreatedFaculty,name='completlytreatedFaculty'),
    path('doctorsch/',views.doctorsch,name='doctorsch'),
    path('successful/',views.successful,name='successful'),
    path('rejectstu/<int:tid>',views.rejectstu,name='rejectstu'),
    path('rejectfac/<int:tid>',views.rejectfac,name='rejectfac')
    
]
