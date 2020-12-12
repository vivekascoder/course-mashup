from rest_framework import serializers
from .models import CourseHub



class CourseHubSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseHub
        fields = '__all__'
