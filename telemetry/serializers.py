from rest_framework import serializers
from .models import BatteryLog, TemperatureLog, DistanceLog, VisionLog
class BatteryLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = BatteryLog
        fields = '__all__'


class TemperatureLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = TemperatureLog
        fields = '__all__'

class DistanceLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = DistanceLog
        fields = '__all__'

class VisionLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = VisionLog
        fields = '__all__'