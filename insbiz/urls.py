from django.urls import path
from django import urls
from .import views

app_name="insbiz"

urlpatterns=[
    path('', views.dashboard, name="dashboard"),
    path('payslip', views.payslip, name="payslip"),
    path('enddate', views.enddate, name="enddate"),
    path('removed', views.removed, name="removed"),
    path('added', views.added, name="added"),
    path('paymenthistory', views.paymenthistory, name="paymenthistory"),
]
