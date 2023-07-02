from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('blood-donation-form',views.donateBlood, name='blood-donation-form'),
    path('news-details/<str:pk>',views.newsDetails, name='news-details'),
    path('program-details/<str:pk>',views.programDetails, name='program-details'),
    path('explore-details/<str:pk>',views.exploreDetails, name='explore-details'),
    path('fest-details/<str:pk>',views.festDetails, name='fest-details'),
    path('community-details/<str:pk>',views.communityDetails, name='community-details'),
    path('loginpage',views.loginPage, name='loginpage'),
    path('logoutUser',views.logoutUser, name='logoutUser'),
    path('blood-donation-admin',views.donateBloodAdmin, name='blood-donation-admin'),
    path('bloodreq-del/<str:pk>',views.bloodreqDel, name='bloodreq-del'),
    path('blood-donated-add/<str:pk>',views.bloodDonatedAdd, name='blood-donated-add'),
    path('blood-donation-response',views.donateBloodRes,name='blood-donation-response'),
]
