from django import forms
from employee.models import Employee  as Emodel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Emodel
        fields = "__all__"
