from django.urls import path
from .views import CourseView, AddCourseView, CourseDetailView

urlpatterns = [
    path('course/<str:lg_tag>/<str:cor_tag>/', CourseView.as_view()),
    path('add/', AddCourseView.as_view()),
    path('detail/<int:pk>/', CourseDetailView.as_view())
]
