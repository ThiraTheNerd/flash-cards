from django.shortcuts import render ,redirect
from rest_framework import serializers
from .models import  Course
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import FlashSerializer

# Create your views here.

@login_required(login_url= '/accounts/login/')
def flash_post(request):
    flash = Course.objects.all()
    if request.method == 'POST':
        return redirect('homepage')


class FlashList(APIView):
    def get(self , request , format = None):
        all_flash = Course.objects.all()
        serializers = FlashSerializer(all_flash , many=True)
        return Response(serializers.data)