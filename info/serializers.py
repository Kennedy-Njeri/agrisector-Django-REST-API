from rest_framework import serializers
from .models import Info


class InfoSerializer(serializers.ModelSerializer):
    """Info serializer"""
    class Meta:
        model = Info
        fields = ("crop", "season", "grow_time", "to", "period")

