from lib2to3.pgen2.token import OP
from statistics import mode
from django.db import models
from apps.opportunities.models import Opportunity
from apps.employees.models import Employee


class TeamAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    potential_needed_number_of_employees = models.IntegerField(blank=True, null=True)
    project = models.ForeignKey(Opportunity, models.DO_NOTHING)

    class Meta:
        db_table = 'team_assignment'

    def __str__(self):
        return self.name


class Assignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    status = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    team_assignment = models.ForeignKey(TeamAssignment, models.DO_NOTHING)

    class Meta:
        db_table = 'assignment'

    def __str__(self):
        return self.name


