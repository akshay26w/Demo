from django.shortcuts import render,redirect
from employee.models import Employee as Emodel
from employee.forms import EmployeeForm
from django.http import HttpResponse
#http://localhost:8000/emp

def show(request):
    employees = Emodel.objects.all()
    form = EmployeeForm()
    return render(request, "empinfo.html", {'employees': employees,'form':form})


def persist_or_update_emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save()
    return redirect('/emp')


def edit_emp(request,id):
    employee = Emodel.objects.get(id=id)
    employees = Emodel.objects.all()
    form = EmployeeForm()
    print(employee.ename)
    form.initial['eid'] = employee.eid
    form.initial['ename'] = employee.ename
    form.initial['eaddress'] = employee.eaddress
    form.initial['eage'] = employee.eage
    form.initial['econtact'] = employee.econtact
    form.initial['esalary'] = employee.esalary
    form.initial['eemail'] = employee.eemail
    return render(request, 'empinfo.html', {'employee': employee,'employees': employees,'form':form})

def delete_emp(request):
    employee = Emodel.objects.get(id=id)
    employee.delete()
    return redirect("/show")



