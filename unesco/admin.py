from django.contrib import admin
from unesco.models import Site, Category, States, Region, Iso


# Register your models here.
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(States)
admin.site.register(Region)
admin.site.register(Iso)