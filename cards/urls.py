from .views import CourseView

from django.conf.urls import url , include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "cards"

# app_name will help us do a reverse look-up latter.

urlpatterns =[
    # path('',views.flash_post , name='homepage'),
    path('course/',views.FlashList.as_view()),
    path('course/<int:pk>', views.CardDescription.as_view())
    path('course/', CourseView.as_view()),

]