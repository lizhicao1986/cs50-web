from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Pizza, Sub

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user,
        "Pizza": Pizza.objects.all(),
        "Sub": Sub.objects.all()
    }
    return render(request, "orders/index.html", context)

def place_order(request):
    context = {
            "user": request.user,
            "Pizza": Pizza.objects.all(),
            "Sub": Sub.objects.all()
    }
    return render(request, "orders/place_order.html", context)
# def Order(request, order_id):
#     try:
#         thisOrder = order.objects.get(pk=order_id)
#     except order.DoesNotExist:
#         raise Http404("Order does not exist")
#     context = {
#         "order": thisOrder
#         #"passengers": flight.passengers.all(),
#         #"non_passengers": Passenger.objects.exclude(flights=flight).all()
#     }
#     return render(request, "orders/order.html", context)

# def book(request, flight_id):
#     try:
#         passenger_id = int(request.POST["passenger"])
#         flight = Flight.objects.get(pk=flight_id)
#         passenger = Passenger.objects.get(pk=passenger_id)
#     except KeyError:
#         return render(request, "flights/error.html", {"message": "No selection."})
#     except Flight.DoesNotExist:
#         return render(request, "flights/error.html", {"message": "No flight."})
#     except Passenger.DoesNotExist:
#         return render(request, "flights/error.html", {"message": "No passenger."})
#     passenger.flights.add(flight)
#     return HttpResponseRedirect(reverse("flight", args=(flight_id,)))
