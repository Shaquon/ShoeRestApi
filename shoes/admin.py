from django.contrib import admin
from shoes.models import Shoe, ShoeType, ShoeColor, Manufacturer

admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)
