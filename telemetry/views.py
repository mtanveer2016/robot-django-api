from rest_framework import generics
from .models import BatteryLog, TemperatureLog, DistanceLog, VisionLog
from .serializers import BatteryLogSerializer, TemperatureLogSerializer, DistanceLogSerializer, VisionLogSerializer




class BatteryLogList(generics.ListCreateAPIView):
    queryset = BatteryLog.objects.all()
    serializer_class = BatteryLogSerializer


class TemperatureLogList(generics.ListCreateAPIView):
    queryset = TemperatureLog.objects.all()
    serializer_class = TemperatureLogSerializer

class DistanceLogList(generics.ListCreateAPIView):
    queryset = DistanceLog.objects.all()
    serializer_class = DistanceLogSerializer

class VisionLogList(generics.ListCreateAPIView):
    queryset = VisionLog.objects.all()
    serializer_class = VisionLogSerializer