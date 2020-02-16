from django.contrib import admin
from .models import Broduct, Woffer

# Register your models here.


class BroductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')


admin.site.register(Broduct, BroductAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Woffer, OfferAdmin)
