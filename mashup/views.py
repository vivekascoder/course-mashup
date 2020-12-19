from .serializers import CourseHubSerializers
from .models import CourseHub
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView

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


class AddCourseView(APIView):
    """
    Add course  in CourseHub
    """

    def post(self, request, format=None):
        print(request.data)
        serializer = CourseHubSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class CourseDetailView(APIView):
    """
    Retrieve, Update, Delete a Course instance
    """
    def get_object(self, pk):
        try:
            return CourseHub.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseHubSerializers(course)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseHubSerializers(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



