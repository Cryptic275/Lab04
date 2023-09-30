from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate = 15 #15 %

def default(request):
    return render(request, "labApp/default.html")

def calculate(request, num):
    return render(request, "labApp/calculate.html", {"number": num, "tax": tax_rate, "after_tax":((num*tax_rate) / 100) + num})

def tax(request):
    return render(request, "labApp/tax.html", {"tax":tax_rate})
