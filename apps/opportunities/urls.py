from django.urls import path
from apps.opportunities import views

urlpatterns = [
    # path('opps/', views.opps, name='opps'),
    path('opps/', views.OpportunityList.as_view(), name='opps'),
    path('opps/<int:pk>/update/', views.OpportunityEdit.as_view(), name='opportunity-update'),

]
