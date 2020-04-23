from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"todo_app\index.html")

def out(request):
    return render(request,"todo_app\out.html")

