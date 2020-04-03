from django.shortcuts import render
from . import views
from .models import dbinfo
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def home(request):
    passwd=''
    return render(request,'home.html',{'pass':passwd})

def student(request):
    download = dbinfo.objects.all()
    return render (request, 'student.html' ,{"downloadc":download})

def teacher(request):
    passwd = request.GET['passwd']
    passwd = str(passwd)
    if(passwd !="1234"):
      return render (request,'home.html',{'pass':"invalid credentials","alert":" "})
    else:
      download = dbinfo.objects.all()
      return render (request,'teacher.html',{"downloadc":download})

def upload(request):
     try:
      booktitle = request.POST['less']
      bookdesc = request.POST['txt']
     except MultiValueDictKeyError:
      booktitle = False
      bookdesc = False
     data = dbinfo(subjectname=booktitle,subject=bookdesc)
     data.save()
     download = dbinfo.objects.all()
     return render(request,'teacher.html',{"alert":"submitted","downloadc":download})

def test(request):
    file = open("subjectfile.txt","r")
    questions = []
    for x in file:
      questions.append(x)
    return render(request,'test.html',{"questions":questions})
      

     