from rest_framework import serializers

class WidthHeightSerializer(serializers.Serializer):
    width = serializers.IntegerField(required=True)
    height = serializers.IntegerField(required=True)