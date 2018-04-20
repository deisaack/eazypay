from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Traffic, PageRequest

class TraficAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip', 'path', 'created' )

admin.site.register(Traffic, TraficAdmin)
admin.site.register(PageRequest)
