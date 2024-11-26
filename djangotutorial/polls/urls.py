from django.urls import path

from . import views
from . import newtest

urlpatterns = [
    path("", views.index, name="index"),
    path("test", newtest.index, name="index")
]
