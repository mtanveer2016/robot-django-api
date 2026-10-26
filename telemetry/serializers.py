from rest_framework import serializers
from .models import BatteryLog
class BatteryLogSerializer(serializers.ModelSerializer):
    # This formats the date into a nice string
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S") 

    class Meta:
        model = BatteryLog
        fields = '__all__'