from rest_framework import serializers, status
# from rest_framework.fields import CurrentUserDefault
from .models import UserCourse
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
class CourseAddSerializer(serializers.ModelSerializer):

    course_collection = serializers.JSONField()


    class Meta:
        model = UserCourse
        fields = ['name', 'lang_tag', 'module', 'course_tag', 'course_collection', 'rating']

class CourseAddMeSerializer(serializers.ModelSerializer):
    lang_tag = serializers.CharField(max_length=10, write_only=True)
    course_tag = serializers.CharField(max_length=10, write_only=True)

    class Meta:
        model = UserCourse
        fields = ['lang_tag', 'course_tag']

    def validate(self, attrs):
        print(attrs)
        lg_tag = attrs.get('lang_tag', "")
        cor_tag = attrs.get('course_tag', "")

        if bool(lg_tag) and bool(cor_tag):
            lang_tag = lg_tag
            course_tag = cor_tag
        elif cor_tag == '':
            course_tag = lg_tag
        else:
            return ValidationError("length required", code=401)
        return super().validate(attrs)
