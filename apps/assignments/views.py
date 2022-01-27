from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import requests
from .models import Assignment
from .forms import NewAssignmentForm
from django.shortcuts import render, redirect
from apps.employees.models import Employee

def assignments_detail(request):
    assignment = Assignment.objects.all()[0]
    context = {'assignment': assignment}
    html_template = loader.get_template('home/assignment_detail.html')
    return HttpResponse(html_template.render(context, request))

def new_assignment(request):

    if request.method == "POST":
        form = NewAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            print('hfhfhfhhf')

        else:
            print('NOOO')
            msg = 'Form is not valid'
    else:
        form = NewAssignmentForm()
    emps = Employee.objects.all()
    return render(request, "home/new_assignment.html", {"form": form, 'emps': emps})
