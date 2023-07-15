from django.urls import path
from . import views
from .custom_admin import blood_donation_admin_site , communities_admin_site ,fests_admin_site


urlpatterns = [
    path('',views.home, name='home' ),
    path('blood-donation-form',views.donateBlood, name='blood-donation-form'),
    path('news-details/<slug:pk>',views.newsDetails, name='news-details'),
    path('program-details/<slug:pk>',views.programDetails, name='program-details'),
    path('explore-details/<slug:pk>',views.exploreDetails, name='explore-details'),
    path('fest-details/<slug:pk>',views.festDetails, name='fest-details'),
    path('community-details/<slug:pk>',views.communityDetails, name='community-details'),
    path('club-details/<slug:pk>',views.clubDetails, name='club-details'),

    path('blood-donation-response',views.donateBloodRes,name='blood-donation-response'),
    #admin
    path('admin/blood',blood_donation_admin_site.urls,name='blood'),
    path('admin/communities',communities_admin_site.urls,name='com'),
    path('admin/fests',fests_admin_site.urls,name='fest'),
    
]
