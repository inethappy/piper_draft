
from django.urls import path
from apps.assignments import views

urlpatterns = [
    path('assignments/detail', views.assignments_detail),
    path('new_assignment', views.new_assignment),
]
