from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseAddSerializer, CourseAddMeSerializer
from .models import UserCourse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CourseAddView(ListCreateAPIView):
    serializer_class = CourseAddSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserCourse.objects.all() 

    def perform_create(self, serializer):
        return serializer.save(profile=self.request.user)



class AddMeCourseViewApi(GenericAPIView):
    serializer_class = CourseAddMeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data())
        lang_tag = serializer.validated_data['lang_tag']
        course_tag = serializer.validated_data['course_tag']

        deployed_course = UserCourse.objects.filter(lang_tag=lang_tag, course_tag=course_tag)[0]
        if deployed_course.profile == request.user:
            deployed_course.id = None
            deployed_course.pk = None
            deployed_course.profile =  request.user
            deployed_course.save()
        else:
            return Response({'success': False, 'message': 'paglet'}, status=status.HTTP_200_OK)

        # fork_course = UserCourse.objects.create(
        #     profile=request.user,
        #     name=deployed_course.name,
        #     lang_tag=deployed_course.lang_tag,
        #     module=deployed_course.module,
        #     course_tag=deployed_course.course_tag,
        #     course_collection=deployed_course.course_collection,
        #     rating=deployed_course.rating,
        #     )

        return Response({'success': True, 'message': 'Congrates man you are now in'}, status=status.HTTP_200_OK)