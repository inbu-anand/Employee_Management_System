from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Employee


# Create your views here.

def index(request):
    employee=Employee.objects.all()
    return render(request,'emsapp/index.html',{'emp':employee})

def view_info(request,id):
    emp=Employee.objects.get(pk=id)
    return render(request,'emsapp/index.html',{'emp':emp})

def add_employee(request):
    if request.method=="POST":
        empnumber=request.POST['empnumber']
        empname=request.POST['empname']
        empmail=request.POST['empmail']
        empcity=request.POST['empcity']
        Employee.objects.create(
            empnumber=empnumber,
            empname=empname,
            empmail=empmail,
            empcity=empcity,
        )
        return redirect(reverse('index'))
    return redirect (reverse('index'))


def delete_employee(request,id):
    if request.method=="POST":
        emp=Employee.objects.get(id=id)
        emp.delete()
    return redirect(reverse('index'))

def update_employee(request,id):
    emp=Employee.objects.get(id=id)

    if request.method=="POST":
        emp.empnumber=request.POST['empnumber']
        emp.empname=request.POST['empname']
        emp.empmail=request.POST['empmail']
        emp.empcity=request.POST['empcity']

        emp.save()

        return redirect(reverse('index'))
    return render(request,'emsapp/index.html',{
        'emp':Employee.objects.all(),
        'emp_to_update':emp
    })
