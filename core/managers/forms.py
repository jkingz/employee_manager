from django import forms
from crispy_forms.helper import FormHelper

from managers.models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'emp_code', 'position',)
        labels = {
            'fullname': 'Full name',
            'emp_code': 'Emp.code',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "SELECT"
