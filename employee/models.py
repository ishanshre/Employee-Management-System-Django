from django.db import models
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    date_Created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('employee:employee_detail', kwargs={'pk':self.pk})