from django.shortcuts import render
from django.http import HttpResponse
from .models import AllCourse

def course(request):
    return render(request, 'Courses/course.html')

def course_list(request):
    courses = AllCourse.objects.all()
    return render(request, 'Courses/course.html', {'courses': courses})