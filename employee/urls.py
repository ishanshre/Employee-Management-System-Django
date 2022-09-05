from django.urls import path
from .views import IndexView, EmployeeListView, EmployeeDetailView, EmployeeCreateView, EmployeeEditView, EmployeeDeleteView, EmployeeFilterListView

app_name = 'employee'
urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    path('employee_filter/', EmployeeFilterListView.as_view(), name='employee_filter'),
    path('employee_list/<int:pk>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee_list/<int:pk>/update/', EmployeeEditView.as_view(), name='employee_update'),
    path('employee_list/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee_create/', EmployeeCreateView.as_view(), name='employee_create'),
]