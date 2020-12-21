from .serializers import CourseHubSerializers, AddCourseSerializer
from .models import CourseHub
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView

class CourseView(APIView):
    """
    List all courses based on tags and create new course
    """
    # permission = (permissions.IsAuthenticated)

    def get(self, request, lg_tag, cor_tag):
        try:
            if bool(lg_tag) and bool(cor_tag):
                lang_tag = lg_tag
                course_tag = cor_tag
            elif cor_tag == '':
                course_tag = lg_tag
            else:
                return Response(status=status.HTTP_411_LENGTH_REQUIRED)    
            course = CourseHub.objects.filter(lang_tag=lg_tag, course_tag=cor_tag)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = CourseHubSerializers(course, many=True)
        return Response(serializer.data)

class AddCourseView(CreateAPIView):
    queryset = CourseHub.objects.all()
    serializer_class = AddCourseSerializer

class CourseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CourseHub.objects.all()
    serializer_class = AddCourseSerializer

