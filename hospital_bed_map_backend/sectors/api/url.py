from django.urls import re_path
from .views import SectorsView, TypeAccommodationView, SectorView

urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', SectorsView.as_view()),
    re_path('acomodacoes', TypeAccommodationView.as_view()),
    re_path(r'^setor/(?P<id>\d+)/$', SectorView.as_view())
]