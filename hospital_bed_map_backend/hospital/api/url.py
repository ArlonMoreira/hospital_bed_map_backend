from django.urls import re_path
from .views import HospitalView

urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', HospitalView.as_view()),
]