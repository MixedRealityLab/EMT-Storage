from django.contrib import admin
from .models import Collection, Exhibit, Module

admin.site.register(Collection)
admin.site.register(Exhibit)
admin.site.register(Module)