from django.urls import path
from .views import BatteryLogList
urlpatterns = [path('battery/', BatteryLogList.as_view())]