from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from orders.views import index
# Create your views here.

# def index(request):
#     if not request.user.is_authenticated:
#         return render(request, "users/login.html", {"message": None})
#     context = {
#         "user": request.user
#     }
#     return render(request, "orders/index.html", context)
#
# def login_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "users/login.html", {"message": "Invalid credentials."})
#
# def logout_view(request):
#     logout(request)
#     return render(request, "users/login.html", {"message": "Logged out."})



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'
