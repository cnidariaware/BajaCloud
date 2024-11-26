from django.urls import path

from . import views
# , newtest, getAppointments, selectAppointment


urlpatterns = [
    path("", views.index, name="index"),
    # path("test", newtest.index, name="index"),
    # path("getSchedule", getAppointments.index, name="index"),
    # path("postSelectAppointment", selectAppointment.index, name="index"),
]
