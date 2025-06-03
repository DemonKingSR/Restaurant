from django.contrib import admin
from .models import customer, staff, order, menu 
admin.site.register(customer)
admin.site.register(staff)
admin.site.register(order)
admin.site.register(menu)


