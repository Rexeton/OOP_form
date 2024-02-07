from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import MyFormView

landing_name = 'landing'
urlpatterns = [
    # path('landing/', include('landing.urls')),
    path('1/', MyFormView.as_view(), name='template'),
]