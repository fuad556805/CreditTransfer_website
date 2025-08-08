from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ewu(request):
    return render(request,'common/base.html')


