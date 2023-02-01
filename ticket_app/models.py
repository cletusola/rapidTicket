from django.db import models
from datetime import date 
import PIL 




# movie model
class Movie(models.Model):

    title = models.CharField(max_length=150, verbose_name="Title", null=False, blank=False)
    description = models.TextField(verbose_name="Description", null=False, blank=False)
    genre = models.CharField(max_length=100, verbose_name="Genre", null=False, blank=False)
    rated = models.CharField(max_length=10, verbose_name="Rated", null=False, blank=False)
    running_time = models.CharField(max_length=30, verbose_name="Running Time", null=False, blank=False)
    release_date = models.CharField(max_length=40, verbose_name="Release Date", null=False, blank=False)
    cast = models.TextField(verbose_name="Cast & Crew", null=False, blank=False)
    directed_by = models.TextField(verbose_name="Directed By", null=False, blank=False)
    produced_by = models.TextField(verbose_name="Produced By", null=False, blank=False)
    show_date = models.CharField(max_length=20, verbose_name="Show Date", null=True, blank=True)
    image = models.ImageField(upload_to=f"images/{date.today()}", verbose_name="Movie Image", null=False, blank=False)
    thriller = models.URLField(max_length=1000, verbose_name="Thriller URL", null=False, blank=False)
    ticket_price = models.IntegerField(verbose_name="Price", null=True, blank=True)
    coming_soon = models.BooleanField(default=False, null=True, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)   


    class Meta:
        ordering = ['-uploaded_on']

    def __str__(self):
        return self.title


    # Setting default image size 
    def save(self, *args, **kwargs):
        super().save()
        img = PIL.Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_imgSize = (300,300)
            img.thumbnail(new_imgSize)
            img.save(self.image.path) 




# order model 
class Order(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    movie_title = models.CharField(max_length=150, verbose_name="Title", null=False, blank=False)
    no_of_ticket = models.CharField(max_length=100, verbose_name="No_of_Ticket", null=False, blank=False)
    tx_ref = models.CharField(max_length=90, verbose_name="Tx Ref", null=False, blank=False)
    flw_ref = models.CharField(max_length=90, verbose_name="Tx Ref", null=False, blank=False)
    card_number = models.CharField(max_length=8, verbose_name="Card Number", null=False, blank=False)
    card_issuer = models.CharField(max_length=40, verbose_name="Card Issuer", null=False, blank=False)
    card_country = models.CharField(max_length=40, verbose_name="Card Country", null=False, blank=False)
    card_type = models.CharField(max_length=30, verbose_name="Card Type", null=False, blank=False)
    card_expiring = models.CharField(max_length=5, verbose_name="Card Expiring Date", null=False, blank=False)
    name = models.CharField(max_length=100, verbose_name="Name", null=False, blank=False)
    email = models.EmailField(max_length=150, verbose_name="email", null=False, blank=False)
    phone = models.CharField(max_length=20, verbose_name="Phone", null=False, blank=False)
    amount = models.CharField(max_length=50, verbose_name="Amount", null=False, blank=False)
    status = models.CharField(max_length=30, verbose_name="Status", null=False, blank=False)
    date_ordered = models.CharField(max_length=40, verbose_name="Date", null=False, blank=False)  
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)  



    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.movie_title