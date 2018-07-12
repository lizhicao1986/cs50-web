from django.contrib import admin

# Register your models here.
from .models import order, pizza, subs, toppings
admin.site.register(order)
admin.site.register(pizza)
admin.site.register(subs)
admin.site.register(toppings)
