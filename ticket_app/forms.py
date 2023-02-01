from django import forms 
from .models import Order




class OrderForm(forms.Form):
    name = forms.CharField(max_length=50, label="Name", required=True)
    email = forms.EmailField(max_length=130, label="Email", required=True)
    phone = forms.CharField(max_length=20, label="Phone", required=True)
    no_of_ticket = forms.CharField(min_length=1, label="No. of Tickets", required=True)

