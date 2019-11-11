from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import FormView, TemplateView, View

from managers.forms import EmployeeForm
from managers.models import Employee


class HomeView(TemplateView):
    ''' Views for home
    '''
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = EmployeeForm()
        context["form"] = form
        return context

    def post(self, *args, **kwargs):
        form = EmployeeForm(self.request.POST)
        if form.is_valid():
            form.save()
            return redirect('managers:list')
        context = {
            'form': form,
        }
        return render(self.request, self.template_name, context)

class EmployeeEditView(TemplateView):
    ''' Views for editing/updating employee
    '''
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeEditView, self).get_context_data(**kwargs)
        employees = Employee.objects.get(id=kwargs['id'])
        form = EmployeeForm(instance=employees)
        context = {
            'employees': employees,
            'form': form
        }
        return context

    def post(self, *args, **kwargs):
        employees = Employee.objects.get(id=kwargs['id'])
        form = EmployeeForm(self.request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('managers:list')
        return redirect('managers:edit', id=kwargs['id'])


class EmployeeListView(TemplateView):
    ''' Views for list of Employees
    '''
    template_name = 'employee_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context["employee_list"] = Employee.objects.all().order_by('-date_created')
        return context


class EmployeeDeleteView(View):

    def post(self, *args, **kwargs):
        # em = Employee.objects.get(id=kwargs['id'])
        em = get_object_or_404(Employee, pk=kwargs['id'])
        em.delete()
        return redirect('managers:list')
