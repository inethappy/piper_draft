from django.contrib import admin
from apps.assignments.models import Assignment, TeamAssignment

admin.site.register(Assignment)
admin.site.register(TeamAssignment)
