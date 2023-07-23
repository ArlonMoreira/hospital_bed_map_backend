from django.contrib import admin
from hospital_bed_map_backend.beds.models import TypeOccupation, Type

# Register your models here.
admin.site.register(TypeOccupation)
admin.site.register(Type)
