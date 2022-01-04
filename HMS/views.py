from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from HMS.models import *
from django.http import HttpResponse
from django.utils.module_loading import import_string
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
import calendar,datetime
from datetime import date


# Create your views here.

def home(req):
    return render(req, 'index.html')

def index(req):
    today = date.today()
    doctordata = DoctorDetails.objects.all()
    d1 = today.strftime("%d %m %Y")
    born = datetime.datetime.strptime(d1, '%d %m %Y').weekday()
    s=calendar.day_name[born]
    schedules=DoctorSchedule.objects.get(Day=s)
    if req.method == 'POST':
        idnum = req.POST['idnum']
        patientnam = req.POST['patient']
        gender = req.POST['Male']
        doctor = req.POST['data']
        age = req.POST['age']
        emailid = req.POST['emailid']
        phone = req.POST['phone']
        problem = req.POST['reason']
        obj = StudentAppointmentForm(idnumber=idnum, name=patientnam, gender=gender, doctor=doctor, age=age,
                                     emailid=emailid, mobile=phone, reason=problem)
        obj.save()
        req.session['studentid'] = obj.id
        treatment = StudentTreatment()
        treatment.doctor = DoctorDetails.objects.get(Name=doctor)
        treatment.appointment = obj
        treatment.save()
        return redirect('successful')
    return render(req, 'patient.html', {'doctordata': doctordata,'schedules':schedules})

def successful(req):
    if req.method=='POST':
        return redirect('home')
    return render(req,'successful.html')


def faculty_appointment(req):
    if req.method == 'POST':
        facultyname = req.POST['patient']
        genders = req.POST['Female']
        Facultyage = req.POST['age']
        emailids = req.POST['emailid']
        mobiles = req.POST['phone']
        doctor = req.POST['data']
        problems = req.POST['reason']
        obj = FacultyAppointmentForm(name=facultyname, gender=genders, doctor=doctor, age=Facultyage, emailid=emailids,
                                     mobile=mobiles, reason=problems)
        obj.save()
        treatment = FacultyTreatment()
        treatment.doctor = DoctorDetails.objects.get(Name=doctor)
        treatment.appointment = obj
        treatment.save()
    return redirect('successful')
    

def doctorlogin(req):
    if req.method == 'POST':
        uname = req.POST['user']
        pwd = req.POST['pass']
        print(uname, pwd)
        try:
            data = DoctorDetails.objects.get(username=uname, Password=pwd)
            req.session['userid'] = data.id
            return render(req, 'DoctorDashboard.html', {'data': data})
        except Exception as e:
            print(e)
            return HttpResponse('wrong credentials')
    return render(req, 'DoctorLogin.html')


def pharmacistlogin(req):
    if req.method == 'POST':
        uname = req.POST['user']
        pwd = req.POST['pass']
        try:
            data = PharmcistDetails.objects.get(username=uname, Password=pwd)
            req.session['userid'] = data.id
            return render(req, 'PharmacistDashBoard.html', {'data': data})
        except Exception as e:
            print(e)
            return HttpResponse('wrong credentials')
    return render(req, 'Pharmacist.html')


def doctordashboard(req):
    return render(req, 'DoctorDashboard.html')


def pharmacistdashboard(req):
    return render(req, 'PharmacistDashBoard.html')


def forgotpassword(req):
    if req.method =='POST':
        mailid=req.POST['email']
        otpnumber=get_random_string(length=6, allowed_chars='123456789')
        receiver=mailid
        msg='OTP FOR PASSWORD RESET=' +''+ ''+otpnumber
        req.session['emailid'] = mailid
        req.session['otp']=otpnumber
        Data=DoctorDetails.objects.filter(email=mailid)
        Dataset=PharmcistDetails.objects.filter(email=mailid)
        if Data:
            EmailMessage(f"Password Reset Mail", msg, to=[mailid]).send()
            return render(req,'Enterotp.html')
        elif Dataset:
            EmailMessage(f"Password Reset Mail", msg, to=[mailid]).send()
            return render(req,'Enterotp.html')
        else:
            return HttpResponse('You entered wrong mail address')
    return render(req,'ForgotPassword.html')



def otppassword(req):
    optnum=req.session['otp']
    if req.method=='POST':
        otpnumbe=req.POST['otpnumber']
        otp=otpnumbe
        if otp==optnum:
            return render (req,'passwordreset.html')
        else:
            return HttpResponse('wrong')


    return render(req,'Enterotp.html')

def passwordreset(req):
    mail=req.session['emailid']
    data=DoctorDetails.objects.filter(email=mail)
    dataset=PharmcistDetails.objects.filter(email=mail)
    if req.method=='POST':
        password=req.POST['pass1']
        cnfpassword=req.POST['pass2']
        if password==cnfpassword:
            if data:
                change=DoctorDetails.objects.get(email=mail)
                change.Password=password
                change.save()
                return HttpResponse('password changed')
            elif dataset:
                 change=PharmcistDetails.objects.get(email=mail)
                 change.Password=password
                 change.save()
            else:
                return HttpResponse('wrong')
        else:
            return HttpResponse('did not change')



def doctoreditprofile(req):
    data = DoctorDetails.objects.get(id=req.session['userid'])
    if req.method == 'POST':
        name = req.POST['name']
        phone = req.POST['mobile']
        usrname = req.POST['username']
        pwd = req.POST['pass']
        pwd1 = req.POST['pass1']
        vil = req.POST['village']
        dis = req.POST['district']
        state = req.POST['state']
        pincode = req.POST['pincode']
        email = req.POST['emailid']
        data.Name = name
        data.email = email
        data.mobile = phone
        data.username = usrname
        data.Password = pwd1
        data.village = vil
        data.District = dis
        data.state = state
        data.pincode = pincode
        data.save()
        print(data.Name)
        print(data.email)
        return render(req, 'DoctorEditprofile.html', {'data':data})
    # user=obj
    # return render(req,'Editprofile.html',{'user':user})
    return render(req, 'DoctorEditprofile.html', {'data': data})


def doctorschedule(req):
    datainfo = DoctorSchedule.objects.all()
    data=DoctorDetails.objects.get(id=req.session['userid'])
    return render(req, 'doctorschedule.html', {'datainfo': datainfo,'data':data})


def pharmacistschedule(req):
    scheduledata = PharmacistSchedule.objects.all()
    data = PharmcistDetails.objects.get(id=req.session['userid'])
    return render(req, 'PharmacistSchedule.html', {'scheduledata': scheduledata,'data':data})


def pharmacisteditprofile(req):
    user = PharmcistDetails.objects.get(id=req.session['userid'])
    data = PharmcistDetails.objects.get(id=req.session['userid'])
    if req.method == 'POST':
        name = req.POST['name']
        phone = req.POST['mobile']
        usrname = req.POST['username']
        pwd = req.POST['pass']
        pwd1 = req.POST['pass1']
        vil = req.POST['village']
        dis = req.POST['district']
        state = req.POST['state']
        pincode = req.POST['pincode']
        email = req.POST['emailid']
        user.Name = name
        user.email = email
        user.mobile = phone
        user.username = usrname
        user.Password = pwd1
        user.village = vil
        user.District = dis
        user.state = state
        user.pincode = pincode
        user.save()
        print(user.Name)
        print(user.email)
        return render(req, 'pharmacistEditprofile.html', {'user': user,'data':data})

    return render(req, 'pharmacistEditprofile.html', {'user': user,'data':data})


def addmedicines(req):
    return render(req, 'addmedicines.html')


def studentsappointments(req):
    doctor = DoctorDetails.objects.get(id=req.session['userid'])
    data=DoctorDetails.objects.get(id=req.session['userid'])
    stu_treatments = StudentTreatment.objects.filter(doctor=doctor, doctor_treated=False, rejected=False)
    return render(req, 'studentappointments.html', {'stu_appointments': stu_treatments,'data':data})

def rejectstu(req,tid):
    data=StudentAppointmentForm.objects.get(id=tid)
    data.delete()
    return redirect('studentsappointments')


def facultyappointments(req):
    doctor = DoctorDetails.objects.get(id=req.session['userid'])
    data=DoctorDetails.objects.get(id=req.session['userid'])
    treatments = FacultyTreatment.objects.filter(doctor=doctor, doctor_treated=False, rejected=False)
    return render(req, 'facultyappointments.html', {'fac_appointments': treatments,'data':data})

def rejectfac(req,tid):
    data=FacultyAppointmentForm.objects.get(id=tid)
    data.delete()
    return redirect('facultyappointments')

def facultymedicines(req):
    data = PharmcistDetails.objects.get(id=req.session['userid'])
    pharmacist = PharmcistDetails.objects.get(id=req.session['userid'])
    treatments = FacultyTreatment.objects.filter(pharmacist=pharmacist, doctor_treated=True, rejected=False,
                                                 completely_treated=False)
    print(treatments)
    return render(req, 'facultmedicines.html', {'fac_appointments': treatments,'data':data})


def studentsmedicines(req):
    data = PharmcistDetails.objects.get(id=req.session['userid'])
    pharmacist = PharmcistDetails.objects.get(id=req.session['userid'])
    stu_treatments = StudentTreatment.objects.filter(pharmacist=pharmacist, doctor_treated=True, rejected=False,
                                                     completely_treated=False)
    return render(req, 'studentmedicines.html', {'stu_appointments': stu_treatments,'data':data})


def handlemedicinespost(req, treatment,type):
    posted_elements = req.POST
    medicines = posted_elements.getlist('medicine')
    count = posted_elements.getlist('count')
    msg = "Medicine\t\t\t\tCount\t\t\t\tMorning\t\t\t\tAfternoon\t\t\t\tEvening\n"
    for i in range(1, len(medicines) + 1):
        if type == 'student':
            medicine = StudentMedicine()
        elif type == 'faculty':
            medicine = FacultyMedicine()
        medicine.treatment = treatment
        medicine.medicine = medicines[i - 1]
        medicine.count = count[i - 1]
        try:
            medicine.morning = True if posted_elements[f'morning{i}'] == 'on' else False
        except MultiValueDictKeyError:
            print(f"No morning for {i}")
        try:
            medicine.afternoon = True if posted_elements[f'afternoon{i}'] == 'on' else False
        except MultiValueDictKeyError:
            print(f"No afternoon for {i}")
        try:
            medicine.night = True if posted_elements[f'night{i}'] == 'on' else False
        except MultiValueDictKeyError:
            print(f"No night for {i}")
        medicine.save()
        msg +=f'{medicine.medicine}\t\t\t\t\t\t{medicine.count}\t\t\t\t{medicine.morning}\t\t\t\t{medicine.afternoon}\t\t\t\t\t{medicine.night}\n'
        print(msg)
    treatment.doctor_treated = True
    treatment.pharmacist = PharmcistDetails.objects.get(Name=posted_elements['pharmacist'])
    treatment.save()
    email = treatment.appointment.emailid
    EmailMessage(f"Medicine details of your appointment-id#{treatment.id}", msg, to=[email]).send()


def addmedicinesforstudent(req, tid):
    treatment = StudentTreatment.objects.get(id=tid)
    data=DoctorDetails.objects.get(id=req.session['userid'])
    today = date.today()
    d1 = today.strftime("%d %m %Y")
    born = datetime.datetime.strptime(d1, '%d %m %Y').weekday()
    s=calendar.day_name[born]
    schedule=PharmacistSchedule.objects.get(Day=s)
    if req.method == 'POST':
        medicine = 'student'
        handlemedicinespost(req, treatment, medicine)
        return HttpResponse("medicins added")
    return render(req, 'addmedicines.html', {'treatment': treatment, 'pharmacists': PharmcistDetails.objects.all(),'data':data,'schedule':schedule})

def addmedicinesforfaculty(req, tid):
    treatment = FacultyTreatment.objects.get(id=tid)
    data=DoctorDetails.objects.get(id=req.session['userid'])
    today = date.today()
    d1 = today.strftime("%d %m %Y")
    born = datetime.datetime.strptime(d1, '%d %m %Y').weekday()
    s=calendar.day_name[born]
    schedule=PharmacistSchedule.objects.get(Day=s)
    if req.method == 'POST':
        medicine = 'faculty'
        handlemedicinespost(req, treatment, medicine)
        return HttpResponse("medicines added")
    return render(req, 'addmedicinesforfaculty.html', {'treatment': treatment, 'pharmacists': PharmcistDetails.objects.all(),'data':data,'schedule':schedule})




def showmedicinesforstudent(req, tid):
    treatment = StudentTreatment.objects.get(id=tid)
    medicines = StudentMedicine.objects.filter(treatment=treatment)
    return render(req, 'viewstudentmedicines.html', {'medicines': medicines, 'treatment': treatment})


def showmedicinesforfaculty(req, tid):
    treatment = FacultyTreatment.objects.get(id=tid)
    medicines = FacultyMedicine.objects.filter(treatment=treatment)
    return render(req, 'viewfacultymedicines.html', {'medicines': medicines, 'treatment': treatment})


def completestudenttreatment(req, tid):
    treatment = StudentTreatment.objects.get(id=tid)
    treatment.completely_treated = True
    treatment.save()
    return redirect('completlytreatedStudents')


def completefacultytreatment(req, tid):
    treatment = FacultyTreatment.objects.get(id=tid)
    treatment.completely_treated = True
    treatment.save()
    return redirect('completlytreatedFaculty')

def completlytreatedStudents(req):
    if req.method=='POST':
        return redirect('studentsmedicines')
    return render(req,'completlyTreatedStudents.html')

def completlytreatedFaculty(req):
    if req.method=='POST':
        return redirect('facultymedicines')
    return render(req,'completlyTreatedFaculty.html')

def doctorsch(req):
    datainfo = DoctorSchedule.objects.all()
    return render(req,'doctorscheduleDsiplay.html',{'datainfo': datainfo})