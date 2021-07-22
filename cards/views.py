from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer


class CourseView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"courses": serializer.data})
    
    def post(self, request):
        course = request.data.get('course')

        # post new projects without admin authorization
        serializer = CourseSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({"success": "Course '{}' created successfully".format(course_saved.title)})