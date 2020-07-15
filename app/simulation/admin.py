from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.objects import Simulation, SimulationData, Arquivo


# Usuario
class SimulationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Simulation._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Simulation._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(Simulation, SimulationAdmin)


class SimulationDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SimulationData._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in SimulationData._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(SimulationData, SimulationDataAdmin)


class ArquivoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Arquivo._meta.get_fields() if f.editable and not f.many_to_many]
    search_fields = [f.name for f in Arquivo._meta.get_fields() if f.editable and not f.many_to_many]
    list_per_page = 15


admin.site.register(Arquivo, ArquivoAdmin)
