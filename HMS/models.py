from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Login(models.Model):
    Username = models.EmailField(blank=True)
    Password = models.CharField(max_length=20)


class DoctorDetails(models.Model):
    Name = models.CharField(max_length=60, unique=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=20, null=True)
    Password = models.CharField(max_length=20, null=True)
    village = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)


class PharmcistDetails(models.Model):
    Name = models.CharField(max_length=60, unique=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10, null=True)
    username = models.CharField(max_length=20, null=True)
    Password = models.CharField(max_length=20, null=True)
    village = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.CharField(max_length=20)


class DoctorSchedule(models.Model):
    Day = models.CharField(max_length=10, unique=True)
    slot1 = models.CharField(max_length=20, null=True)
    slot2 = models.CharField(max_length=20, null=True)
    slot3 = models.CharField(max_length=20, null=True)
    slot4 = models.CharField(max_length=20, null=True)


class PharmacistSchedule(models.Model):
    Day = models.CharField(max_length=10, unique=True)
    slot1 = models.CharField(max_length=20, null=True)
    slot2 = models.CharField(max_length=20, null=True)
    slot3 = models.CharField(max_length=20, null=True)
    slot4 = models.CharField(max_length=20, null=True)


class StudentAppointmentForm(models.Model):
    idnumber = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    doctor = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=20, null=True)
    emailid = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10, null=True)
    reason = models.CharField(max_length=10, null=True)


class FacultyAppointmentForm(models.Model):
    name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    doctor = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=20, null=True)
    emailid = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=10, null=True)
    reason = models.CharField(max_length=10, null=True)


class Treatment(models.Model):
    doctor = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(PharmcistDetails, on_delete=models.CASCADE, null=True)
    doctor_treated = models.BooleanField(default=False)  # Set this to true after doctor adds medicine
    completely_treated = models.BooleanField(default=False)  # Set this to true after medicines are given
    rejected = models.BooleanField(default=False)


class StudentTreatment(Treatment):
    appointment = models.ForeignKey(StudentAppointmentForm, on_delete=models.CASCADE)


class FacultyTreatment(Treatment):
    appointment = models.ForeignKey(FacultyAppointmentForm, on_delete=models.CASCADE)


class Medicine(models.Model):
    medicine = models.CharField(max_length=100)
    count = models.IntegerField()
    morning = models.BooleanField(default=False)
    afternoon = models.BooleanField(default=False)
    night = models.BooleanField(default=False)


class StudentMedicine(Medicine):
    treatment = models.ForeignKey(StudentTreatment, on_delete=models.CASCADE, default=None)


class FacultyMedicine(Medicine):
    treatment = models.ForeignKey(FacultyTreatment, on_delete=models.CASCADE, default=None)
