from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.uslogin, name='login'),
    path('registration', views.usregistration, name='registration'),
    path('register', views.usregister, name='register'),
    path('uslogin', views.urlogin, name='uslogin'),
    path('usersubmitrequest', views.usersubmitrequest, name='usersubmitrequest'),
    path('servicestatus', views.servicestatus, name='servicestatus'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('userchangepassword', views.userchangepassword, name='userchangepassword'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('submitrequestsuccess/<int:request_id>/', views.submit_request_success, name='submitrequestsuccess'),
    
]