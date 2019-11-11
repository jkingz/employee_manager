from django.urls import path

from managers.views import HomeView, EmployeeListView, EmployeeEditView, EmployeeDeleteView

app_name = 'managers'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('employee_list/', EmployeeListView.as_view(), name='list'),
    path('edit/<int:id>', EmployeeEditView.as_view(), name='edit'),
    path('delete/<int:id>', EmployeeDeleteView.as_view(), name='delete'),
]
