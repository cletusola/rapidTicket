from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse 
from django.contrib import messages 

from .models import Movie,Order
from .forms import OrderForm

import math
import random
import requests
import json 




# movies view 
def MovieView(request):
    movie = Movie.objects.filter(coming_soon=False).order_by('-uploaded_on')
    coming_soon = Movie.objects.filter(coming_soon=True).order_by('-uploaded_on')

    context = {
        "movie":movie,
        "coming_soon":coming_soon,
    }
    return render(request, 'pages/home.html', context)

# movies details view 
def MovieDetail(request, id):
    movie = get_object_or_404(Movie, id=id)

    form = OrderForm()
    context = {
        "movie":movie,
        "form":form
    }
    return render(request, 'pages/movie_detail.html', context)



# flutter wave payment function
def process_payment(name, email, amount, phone, movie_id, movie_title, no_of_ticket):
    auth_token= 'YOUR_SECRET_KEY'
    hed = {'Authorization': 'Bearer ' + auth_token}
    data = {
            "tx_ref":''+str(math.floor(10000 + random.random()*900000)),
            "amount":amount,
            "currency":"NGN",
            "redirect_url":"http://localhost:8000/order_response/",
            "payment_options":"card",
            "meta":{
                "movie_id":movie_id,
                "movie_title":movie_title,
                "no_of_ticket": no_of_ticket,
            },
            "customer":{
                "email":email,
                "phonenumber":phone,
                "name":name
            },
            "customizations":{
                "title":"Rapid  Ticket",
                "description":"Purchase Latest Movie Tickets",
            }
            }
    url = ' https://api.flutterwave.com/v3/payments'
    response = requests.post(url, json=data, headers=hed)
    response=response.json()
    link=response['data']['link']
    return link   

# order view 
def OrderView(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            price = request.POST.get('price')
            movie_id = request.POST.get('movie_id')
            movie = Movie.objects.get(id=movie_id)
            movie_title = movie.title 
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            no_of_ticket = form.cleaned_data['no_of_ticket']
            amount = int(price) * int(no_of_ticket)

            try:
                process_payment(name, email, amount, phone, movie_id, movie_title,no_of_ticket)
            except:
                messages.error(request,"Unable to process payment !")
    else:
        form = OrderForm()
    return redirect(reverse('movie_detail' , args=[str(movie_id)]))



# order response view
def OrderResponseView(request):
    status=request.GET.get('status', None)
    tx_ref=request.GET.get('tx_ref', None)
    mydata= json.loads(request.body.decode("utf-8"))
    res_data = mydata["data"]
    res_card = mydata["data"]["card"]
    res_meta = mydata["data"]["meta"]
    res_cus = mydata["data"]["customer"]

    movie_id = res_meta["movie_id"]
    movie = Movie.objects.filter(id=movie_id)
    no_of_ticket = res_meta["no_of_ticket"]
    movie_title = res_meta["movie_title"]
    tx_ref = res_data["tx_ref"]
    flw_ref = res_data["flw_ref"]
    card_first_6 = res_card['first_6digits']
    card_last_4 = res_card['last_4digits']
    card_number = f"{card_first_6}xxxxxxx{card_last_4}"
    card_issuer = res_card["issuer"]
    card_country = res_card["country"]
    card_type = res_card["type"]
    card_expiring = res_card["expiry"]
    name = res_cus["name"]
    phone = res_cus["phone_number"]
    email = res_cus["email"]
    amount = res_data["amount"]
    # status = json_data["status"]
    date = res_data["created_at"]

    movie = Movie(
        movie=movie,
        movie_title = movie_title,
        no_of_ticket = no_of_ticket,
        tx_ref = tx_ref,
        flw_ref = flw_ref,
        card_number = card_number,
        card_issuer = card_issuer,
        card_country = card_country,
        card_type = card_type,
        card_expiring = card_expiring,
        name = name,
        email = email,
        phone = phone,
        amount = amount,
        status = status,
        date_ordered = date

    )
    movie.save()

    return HttpResponse("Order Completed.")







