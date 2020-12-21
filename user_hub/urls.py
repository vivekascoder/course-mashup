from django.urls import path
from .views import CourseAddView, AddMeCourseViewApi

urlpatterns = [
    path('add/', CourseAddView.as_view(), name="user-add"),
    path('addme/', AddMeCourseViewApi.as_view(), name="add_me")
]
