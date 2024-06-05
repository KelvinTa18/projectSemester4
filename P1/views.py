from django.shortcuts import render, redirect
from collections import defaultdict
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Attendance.models import Attendance
from django.core.serializers import serialize
from datetime import datetime, timedelta
from django.contrib.auth import login, logout, authenticate
from Teacher.models import Teacher
from Student.models import Student
from Rate.models import Rate
from Class.models import Class
from django.db.models.functions import TruncMonth
from collections import defaultdict


def dashboard(request):
    # Retrieve all teachers and students
    myteachers = Teacher.objects.all()
    mystudents = Student.objects.all()

    myattendance = Attendance.objects.all()
    myrates = Rate.objects.all()
    myclass = Class.objects.all()

    # Ensure keys exist for both genders in the dictionaries
    teacher_male_count= sum(1 for obj in myteachers if obj.gender == 1)
    teacher_female_count= sum(1 for obj in myteachers if obj.gender == 0)
    student_male_count= sum(1 for obj in mystudents if obj.gender== 1)
    student_female_count= sum(1 for obj in mystudents if obj.gender == 0)
    attendace_present_count = sum(1 for obj in myattendance if obj.status_attendance== 1)
    attendace_absent_count = sum(1 for obj in myattendance if obj.status_attendance== 0)

    # Satisfaction rates (replace these values with actual data)
    
   
    kurang_puas = sum(1 for obj in myrates if obj.rate== 0)/myrates.count()*100
    lumayan_puas = sum(1 for obj in myrates if obj.rate== 1)/myrates.count()*100
    sangat_puas = sum(1 for obj in myrates if obj.rate== 2)/myrates.count()*100


    # Prepare context with all data
    context = {
        'total_teachers': myteachers.count(),  
        'total_students': mystudents.count(), 
        'total_class': myclass.count(),
        'teacher_male_count': teacher_male_count,
        'teacher_female_count': teacher_female_count,
        'student_male_count': student_male_count,
        'student_female_count':student_female_count,
        'attendace_present_count': attendace_present_count,
        'attendace_absent_count': attendace_absent_count,
        'kurang_puas': kurang_puas,
        'lumayan_puas': lumayan_puas,
        'sangat_puas': sangat_puas,
    }

    return render(request, 'dashboard.html', context)


# def dashboard(request):
#     form = {
#         "title": "My Dashboard",
#         "content": "MY CONTENT"
#     }
#     return render(request, "dashboard.html", {'form': form})


def permission_denied(request):
    if request.method == "POST":
        if 'next' in request.POST:
            path = str(request.POST.get('next')).split('/')[1]
            return redirect(f"/{path}")
            # return HttpResponse(f"/{path}")
    else:
        form = {
            "title": "Permission Denied",
            "content": "You dont have permission, Please contact the admin to continue with this action",
        }
        return render(request, "permission_denied.html", {'form': form})
