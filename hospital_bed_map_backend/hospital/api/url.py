from django.urls import re_path
from .views import HospitalView, HospitalViewNoParams

urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', HospitalView.as_view()),
    re_path('cadastrar/', HospitalViewNoParams.as_view()),
]