from django.urls import re_path
from .views import SectorsView, TypeAccommodationView, SectorPutView, SectorDeleteView

urlpatterns = [
    re_path(r'^(?:(?P<hospital>\d+)/)?$', SectorsView.as_view()),
    re_path('acomodacoes', TypeAccommodationView.as_view()),
    re_path(r'^atualizar/(?P<sector>\d+)/$', SectorPutView.as_view()),
    re_path(r'^remover/(?P<sector>\d+)/$', SectorDeleteView.as_view())
]