from rest_framework import serializers
from .models import BatteryLog, TemperatureLog, DistanceLog, VisionLog



class BatteryLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # <-- ADD THIS

    class Meta:
        model = BatteryLog
        fields = '__all__'
        read_only_fields = ['created_at']  # <-- ADD THIS


class TemperatureLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # <-- ADD THIS

    class Meta:
        model = TemperatureLog
        fields = '__all__'
        read_only_fields = ['created_at']  # <-- ADD THIS

class DistanceLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True) 

    class Meta:
        model = DistanceLog
        fields = '__all__'
        read_only_fields = ['created_at']  # <-- ADD THIS

class VisionLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)  # <-- ADD THIS

    class Meta:
        model = VisionLog
        fields = '__all__'
        read_only_fields = ['created_at']  # <-- ADD THIS