from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("place_order", views.place_order, name="place_order"),
    #path("<int:order_id>", views.Order, name="order")
    #path("<int:flight_id>/book", views.book, name="book")
]
