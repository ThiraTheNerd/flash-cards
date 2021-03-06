from django.http.response import Http404
from django.shortcuts import render ,redirect
from rest_framework import serializers
from .models import  Course
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import FlashSerializer, CourseSerializer
from rest_framework import status
# Create your views here.

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


class FlashList(APIView):
    def get(self , request , format = None):
        all_flash = Course.objects.all()
        serializers = FlashSerializer(all_flash , many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers = FlashSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data , status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class CardDescription(APIView):
    def get_card(self , pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        card = self.get_card(pk)
        serializers = FlashSerializer(card)
        return Response(serializers.data)

    def put(self , request ,pk, format= None):
        card = self.get_card(pk)
        serializers = FlashSerializer(card , request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk,format= None):
        card=self.get_card(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

       
def flash_post(request):
    flash = Course.objects.all()
    if request.method == 'POST':
        return redirect('homepage')



