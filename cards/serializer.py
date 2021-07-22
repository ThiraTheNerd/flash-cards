from rest_framework import serializers
from  .models import Course


class FlashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title' , 'body')