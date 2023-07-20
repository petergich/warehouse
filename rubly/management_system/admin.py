from django.contrib import admin
from .models import Capex, Purchase_Orders, SKUs

# Register your models here.
# admin.site.register(User)
admin.site.register(SKUs)
admin.site.register(Purchase_Orders)
admin.site.register(Capex)
