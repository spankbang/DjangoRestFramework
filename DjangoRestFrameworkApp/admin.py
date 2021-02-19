from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeSAdmin(admin.ModelAdmin):
    list_display=[
        'id','eno','ename','esal','eaddr'
    ]

admin.site.register(Employee,EmployeeSAdmin)