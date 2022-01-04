from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Login)
admin.site.register(DoctorDetails)
admin.site.register(PharmcistDetails)
admin.site.register(StudentAppointmentForm)
admin.site.register(StudentTreatment)
admin.site.register(StudentMedicine)
admin.site.register(FacultyTreatment)