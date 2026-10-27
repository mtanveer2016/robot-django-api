from django.db import models
class BatteryLog(models.Model):
    voltage = models.FloatField()
    percentage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

# Add these three:
class TemperatureLog(models.Model):
    temperature_c = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class DistanceLog(models.Model):
    distance_cm = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

class VisionLog(models.Model):
    prompt = models.CharField(max_length=255) 
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)