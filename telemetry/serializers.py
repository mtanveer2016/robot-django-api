from rest_framework import serializers
from .models import BatteryLog
class BatteryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryLog
        fields = '__all__'