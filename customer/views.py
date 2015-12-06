from django.shortcuts import render

from customer.models import Customer


# Create your views here.

def customer_index(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customers.html', {'customers': customers})

