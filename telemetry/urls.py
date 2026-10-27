from django.urls import path
from .views import BatteryLogList, TemperatureLogList, DistanceLogList, VisionLogList

urlpatterns = [
    path('battery/', BatteryLogList.as_view()),
    path('temperature/', TemperatureLogList.as_view()),
    path('distance/', DistanceLogList.as_view()),
    path('vision/', VisionLogList.as_view()),
]