from django import forms
from apps.opportunities.models import Opportunity

class OpportunityDetailForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'