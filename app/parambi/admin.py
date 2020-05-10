from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.objects import RegistroHeader, RegistroDetalhe, Arquivo


# Usuario
class RegistroHeaderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in RegistroHeader._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in RegistroHeader._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(RegistroHeader, RegistroHeaderAdmin)


class RegistroDetalheAdmin(admin.ModelAdmin):
    list_display = [f.name for f in RegistroDetalhe._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in RegistroDetalhe._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(RegistroDetalhe, RegistroDetalheAdmin)


class ArquivoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Arquivo._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Arquivo._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(Arquivo, ArquivoAdmin)
