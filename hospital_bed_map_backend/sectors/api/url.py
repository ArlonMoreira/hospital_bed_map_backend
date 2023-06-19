from django.urls import re_path
from .views import SectorsView, TypeAccommodationView

urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', SectorsView.as_view()),
    re_path('acomodacoes', TypeAccommodationView.as_view())
]