from django.urls import path

from .views import CourseView


app_name = "cards"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('course/', CourseView.as_view()),
]