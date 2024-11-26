from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("""
                        <h1>Thsi is Home Page </h1>
                        <p>This is the second line </p>
                        """)

def contact(request):
    return HttpResponse('This is contact page')
