from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    body = serializers.CharField()