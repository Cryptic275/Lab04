from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="default"),
    path("<int:num>", views.calculate, name="calculator"),
    path("taxrate", views.tax, name="tax rate")
]