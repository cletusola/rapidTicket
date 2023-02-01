from django.contrib import admin
from .models import Movie, Order



class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','genre','rated','ticket_price','uploaded_on']
    list_display_links = ['title','genre','ticket_price','rated']
    list_filter = ['genre', 'rated']

admin.site.register(Movie, MovieAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['movie_title','name','no_of_ticket', 'amount','flw_ref','date_ordered','date'] 
    list_display_links = ['movie_title','name','no_of_ticket', 'amount'] 

admin.site.register(Order,OrderAdmin)

