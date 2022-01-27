from django.contrib import admin
from apps.employees.models import WeeklyCheckIn, Employee

admin.site.register(Employee)
admin.site.register(WeeklyCheckIn)