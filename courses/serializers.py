from rest_framework import serializers
from .models import CourseHub



class CourseHubSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseHub
        fields = '__all__'

class AddCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseHub
        fields = ('name', 'lang_tag', 'module', 'course_tag', 'location_url', 'rating')
        
