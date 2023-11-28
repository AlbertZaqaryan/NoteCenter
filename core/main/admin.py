from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductCPU)
admin.site.register(ProductGPU)
admin.site.register(ProductMemory)
admin.site.register(ProductDisplay)
admin.site.register(ProductRam)