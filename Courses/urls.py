from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('<str:university_name>/', views.university_courses, name='university-courses'),
]
