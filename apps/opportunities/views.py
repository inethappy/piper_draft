from re import L, template
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests
from apps.assignments.forms import TeamAssignmentForm, AssignmentForm

from apps.assignments.models import Assignment, TeamAssignment
from apps.employees.models import Employee
from .models import Opportunity
from django.shortcuts import render, redirect

from apps.opportunities.salesforce_api import SalesforseAPI
from apps.opportunities.forms import OpportunityDetailForm
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from django.forms import inlineformset_factory

TeamInlineFormset = inlineformset_factory(
    Opportunity,
    TeamAssignment,
    form=TeamAssignmentForm,
    # extra=0
)
TeamAssignmentInlineFormset = inlineformset_factory(
    TeamAssignment,
    Assignment,
    form=AssignmentForm,
)

@method_decorator(login_required, name='dispatch')
class OpportunityEdit(UpdateView):
    model = Opportunity
    form_class = OpportunityDetailForm
    template_name = 'opportunities/opps_detail.html'

    def get_context_data(self, **kwargs):
        context = super(OpportunityEdit, self).get_context_data(**kwargs)
        item = Opportunity.objects.filter(name='Ebay')[0]
        print(item.teamassignment_set.all())
        context['team_assignment_formset'] = TeamInlineFormset(instance=item)

        return context

    def form_valid(self, form, team_assignment_formset):
        self.object = form.save()
        self.object.save()

        team_assignments = team_assignment_formset.save(commit=False)
        for meta in team_assignments:
            meta.project = self.object
            meta.save()

        # get_context_data populates object in the context 
        # or you also get it with the name you want if you define context_object_name in the class
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form, team_assignment_formset):
        return self.render_to_response(self.get_context_data(form=form,
                                  team_assignment_formset=team_assignment_formset))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        team_assignment_formset = TeamInlineFormset(self.request.POST)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid() and team_assignment_formset.is_valid():
            return self.form_valid(form, team_assignment_formset)
        else:
            return self.form_invalid(form, team_assignment_formset)
        # return super().post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class OpportunityList(ListView):
    model = Opportunity
    context_object_name = 'opps_list'
    template_name = 'opportunities/opps.html'

    def get_queryset(self):
        """
        Filter objects so a user only sees his own stuff.
        """
        if self.request.user.has_perm('opportunities.view_only_assigned_opportunities'):
            user = Employee.objects.filter(user=self.request.user)[0]
            return Opportunity.objects.filter(scoping_lead=user)
        else:
            return Opportunity.objects.all()
