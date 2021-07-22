from django.conf.urls import url , include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    # path('',views.flash_post , name= 'homepage'),
    path('course/',views.FlashList.as_view()),
]