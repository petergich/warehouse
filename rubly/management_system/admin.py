from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Description)
admin.site.register(Warehouse)
admin.site.register(Purchase_Order)
admin.site.register(IssuanceExternal)
admin.site.register(IssuanceInternal)
admin.site.register(Returns)
admin.site.register(Checkin)

