from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('news/<str:pk>',views.news, name='news'),
    path('program/<str:pk>',views.program, name='program'),
    path('blood-donation-form',views.donateBlood, name='blood-donation-form'),
    path('explore/<str:pk>',views.explore, name='explore'),
    path('fests/<str:pk>',views.fests, name='fests'),
    path('loginpage',views.loginPage, name='loginpage'),
    path('logoutUser',views.logoutUser, name='logoutUser'),
    path('creators',views.creators, name='creators'),
    path('blood-donation-admin',views.donateBloodAdmin, name='blood-donation-admin'),
    path('bloodreq-del/<str:pk>',views.bloodreqDel, name='bloodreq-del'),
    path('blood-donated-add/<str:pk>',views.bloodDonatedAdd, name='blood-donated-add'),
    path('blood-donation-response',views.donateBloodRes,name='blood-donation-response')

]
