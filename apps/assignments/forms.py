from pyexpat import model
from django import forms
from .models import Assignment, TeamAssignment

class NewAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class TeamAssignmentForm(forms.ModelForm):
    class Meta:
        model = TeamAssignment
        fields = '__all__'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
