from django.contrib import admin

# Register your models here.
from ordenamiento.models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo')
    search_fields = ('nombre','tipo')

admin.site.register(Parroquia,ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero_vivien','numero_par','numero_edif','parroquia')
    search_fields = ('num_par','parroquia')

admin.site.register(Barrio,BarrioAdmin)