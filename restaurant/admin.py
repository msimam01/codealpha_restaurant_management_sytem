from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Inventory)
