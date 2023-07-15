from django.urls import path
from . import views
from .custom_admin import blood_donation_admin_site , communities_admin_site ,fests_admin_site


urlpatterns = [
    path('',views.home, name='home' ),
    path('blood-donation-form',views.donateBlood, name='blood-donation-form'),
    path('blood-donation-response',views.donateBloodRes,name='blood-donation-response'),

    
    path('news/<slug:pk>',views.newsDetails, name='news'),
    path('program/<slug:pk>',views.programDetails, name='program'),
    path('explore/<slug:pk>',views.exploreDetails, name='explore'),
    path('fest/<slug:pk>',views.festDetails, name='fest'),
    path('community/<slug:pk>',views.communityDetails, name='community'),
    path('club/<slug:pk>',views.clubDetails, name='club'),

    
    #admin
    path('admin/blood',blood_donation_admin_site.urls,name='blood'),
    path('admin/communities',communities_admin_site.urls,name='com'),
    path('admin/fests',fests_admin_site.urls,name='fest'),
    
]
