from django.contrib import admin

from managers.models import Employee, Position


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'emp_code', 'mobile', 'date_created', 'position',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)
