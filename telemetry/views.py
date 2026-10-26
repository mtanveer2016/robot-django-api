from rest_framework import generics
from .models import BatteryLog
from .serializers import BatteryLogSerializer
class BatteryLogList(generics.ListCreateAPIView):
    queryset = BatteryLog.objects.all()
    serializer_class = BatteryLogSerializer
