from django import forms
from .models import Employee



class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'dept',
            'salary',
            'bonus',
            'role',
            'phone',
            'hire_date',
        ]


class FilterEmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    dept = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)

    class Meta:
        fields = ['name', 'dept', 'role']