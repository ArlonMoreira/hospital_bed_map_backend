from django.urls import re_path
from hospital_bed_map_backend.beds.api.views import BedsView, TypeOccupationView, TypeView

urlpatterns = [
    re_path('cadastrar/', BedsView.as_view()),
    re_path('status/', TypeOccupationView.as_view()),
    re_path('tipo/', TypeView.as_view())
]   