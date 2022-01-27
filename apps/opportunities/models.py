# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.employees.models import Employee, WeeklyCheckIn
from django.contrib.postgres.fields import ArrayField

class Opportunity(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    customer = models.CharField(max_length=100)
    tech_stack = models.TextField(blank=True, null=True)
    scoping_due_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    sow_pdf = models.URLField(blank=True, null=True)
    call_notes = models.TextField(blank=True, null=True)
    call_date = ArrayField(models.DateTimeField(blank=True), blank=True, null=True)
    budget = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    is_opportunity = models.BooleanField(null=False)
    is_project = models.BooleanField(null=False)
    scoping_lead = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, null=True)
    backround_description = models.TextField(blank=True)
    scoping_notes = models.TextField(blank=True)
    sow_review_notes = models.TextField(blank=True)
    resourcing_notes = models.TextField(blank=True)
    company_website_url = models.URLField(blank=True)
    # additional_scoping_team = models.ManyToManyField(Assignment)
    weekly_check_ins = models.ManyToManyField(WeeklyCheckIn, blank=True)

# Estimated Timeline
# Potential Resource Types Needed

    class Meta:
        db_table = 'opportunity'

        permissions = [
            ("view_only_assigned_opportunities", "Can view only opportunities to which user is assigned to."),
        ]

    def __str__(self):
        return self.name

# class Project(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     customer = models.CharField(max_length=100)
#     tech_stack = models.TextField(blank=True, null=True)  # This field type is a guess.
#     scoping_due_date = models.DateField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     type = models.TextField(blank=True, null=True)  # This field type is a guess.
#     sow_pdf = models.BinaryField(blank=True, null=True)
#     call_notes = models.BinaryField(blank=True, null=True)
#     budget = models.CharField(max_length=100, blank=True, null=True)
#     status_project = models.CharField(max_length=50, blank=True, null=True)
#     status_opportunity = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         db_table = 'project'

#     def __str__(self):
#         return self.name




# class History(models.Model):
#     actor = models.ForeignKey(Employee, models.DO_NOTHING, db_column='actor', related_name='actor')
#     id = models.BigAutoField(primary_key=True)
#     verb = models.CharField(max_length=50, blank=True, null=True)
#     recipient = models.ForeignKey(Employee, models.DO_NOTHING, db_column='recipient', related_name='recipient')
#     project = models.ForeignKey(Project, models.DO_NOTHING, db_column='project')
#     date = models.DateField(blank=True, null=True)
#     note = models.TextField(blank=True, null=True)

#     class Meta:
#         db_table = 'history'

