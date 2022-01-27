from django.db import models
# from apps.opportunities.models import Opportunity


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.TextField(max_length=100, blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    department = models.TextField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    employee_type = models.TextField(max_length=100, blank=True, null=True)
    employee_status = models.TextField(max_length=100, blank=True, null=True)
    reporting_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reporting_to', blank=True, null=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.name


class WeeklyCheckIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    week_end_date = models.DateField(blank=True, null=True)
    wellness_survey = models.IntegerField(blank=True, null=True)
    wellness_thoughts = models.TextField(blank=True, null=True)
    # project = models.ManyToManyField(Opportunity)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'weekly_check_in'

    def __str__(self):
        return self.name

    def get_projects(self):
        return [p.name for p in self.project.all()]
