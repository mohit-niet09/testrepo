from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acc_demo(request):
    students = [
        {'name': 'Mohit', 'age': 35},
        {'name': 'Abhinav', 'age': 12},
        {'name': 'Manjeet', 'age': 25},
        {'name': 'Aman', 'age': 16},
        {'name': 'Manjeet', 'age': 25},
        {'name': 'Aman', 'age': 16},
    ]
    return render(request, 'index.html', context={'test':students})

def demo():
    return 'test data'