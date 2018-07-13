from django.contrib import admin

# Register your models here.
from .models import Pizza, Sub
admin.site.register(Pizza)
admin.site.register(Sub)
