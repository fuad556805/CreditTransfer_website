from django.shortcuts import render
from .models import AllCourse

def course(request):
    return render(request, 'Courses/course.html')

def course_list(request):
    courses = AllCourse.objects.all()
    return render(request, 'Courses/course.html', {'courses': courses})

def university_courses(request, university_name):
    courses = AllCourse.objects.filter(university_name=university_name)
    return render(request, 'Courses/course.html', {
        'courses': courses,
        'selected_university': university_name
    })
