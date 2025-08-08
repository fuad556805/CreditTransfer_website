from django.contrib import admin
from .models import AllCourse, University

@admin.register(AllCourse)
class AllCourseAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'course_code', 'course_name')

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_name',)
