from django.contrib import admin
from .models import *

# all the registerations of the entities for the django administrations
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(ProductOrder)
admin.site.register(Major)
admin.site.register(Condition)
admin.site.register(Faq)
admin.site.register(School)
admin.site.register(ContactUser)