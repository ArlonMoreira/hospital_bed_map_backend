from django.urls import re_path
from hospital_bed_map_backend.beds.api.views import BedsUpdateStatusView, BedsListView, BedsView, TypeOccupationView, TypeView

urlpatterns = [
    re_path(r'^listar/(?P<sector>\d+)/$', BedsListView.as_view()),
    re_path('cadastrar/', BedsView.as_view()),
    re_path('status/', TypeOccupationView.as_view()),
    re_path(r'^occupation/(?P<bed>\d+)/$', BedsUpdateStatusView.as_view()),
    re_path('tipo/', TypeView.as_view())
]   