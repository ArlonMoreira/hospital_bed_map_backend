from django.urls import re_path
from hospital_bed_map_backend.beds.api.views import BedsView

urlpatterns = [
    re_path('cadastrar/', BedsView.as_view()),
]