from django.urls import re_path
from .views import SectorsView

urlpatterns = [
    re_path(r'^(?:(?P<id>\d+)/)?$', SectorsView.as_view())
]