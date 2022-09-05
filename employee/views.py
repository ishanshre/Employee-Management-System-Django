from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from django.views import View
from .models import Employee, Role, Department
from .forms import EmployeeCreateForm, FilterEmployeeForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'employee/index.html'
    def get(self, request):
        return render(request, self.template_name)
    

class EmployeeListView(generic.ListView):
    model = Employee
    context_object_name = 'employee_list'
    template_name = 'employee/employee_list.html'

    def get_queryset(self):
        return self.model.objects.all()
    

class EmployeeDetailView(generic.DetailView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee/employee_detail.html'


class EmployeeCreateView(SuccessMessageMixin ,CreateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee/employee_create.html'
    message = 'New Employee Added'

    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message
    
class EmployeeEditView(SuccessMessageMixin, UpdateView):
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee/employee_update.html'
    message = "Employee Updated"
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message

class EmployeeDeleteView(SuccessMessageMixin, DeleteView):
    model = Employee
    template_name = 'employee/employee_delete.html'
    message = "Employee Deleted"
    success_url = reverse_lazy('employee:employee_list')
    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return self.message


class EmployeeFilterListView(View):
    model = Employee
    template_name = 'employee/employee_filter.html'
    def get(self, request, *args, **kwargs):
        name = self.request.GET.get('name')
        dept = self.request.GET.get('dept')
        role = self.request.GET.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            'emps':emps
        }
        return render(request, self.template_name, context)