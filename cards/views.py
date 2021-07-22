from django.shortcuts import render ,redirect
from .models import  Course
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url= '/accounts/login/')
def flash_post(request):
    flash = Course.objects.all()
    if request.method == 'POST':
        return redirect('homepage')
