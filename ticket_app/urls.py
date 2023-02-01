from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 

from .views import MovieView,MovieDetail,OrderView,OrderResponseView


urlpatterns = [
    path('', MovieView, name="home"),
    path('movie/<int:id>/', MovieDetail, name="movie_detail"),
    path('order/', OrderView, name="order"),
    path("order_response/", OrderResponseView, name="order_response" )

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)