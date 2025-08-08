# Equivalencies/views.py

from django.shortcuts import render
from .models import SimilarCourse  # import model

def equivalance(request):
    courses = SimilarCourse.objects.all()  # fetch all data
    return render(request, 'Equivalencies/equi.html', {'courses': courses})
