from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self,*args,**kwargs):

        help ="create groups and default users"

        group_community, created = Group.objects.get_or_create(name='community')
        group_blood, created = Group.objects.get_or_create(name='bloodDonation')
        group_fest, created = Group.objects.get_or_create(name='fest')

        permission_blood = Permission.objects.filter(codename__in=[
            'add_blooddonatedstudents',
            'change_blooddonatedstudents',
            'delete_blooddonatedstudents',
            'view_blooddonatedstudents',
            'add_blooddonation',
            'change_blooddonation',
            'delete_blooddonation',
            'view_blooddonation',
            'add_bloodreq',
            'change_bloodreq',
            'delete_bloodreq',
            'view_bloodreq',
            ])

        permission_community = Permission.objects.filter(codename__in=[
            'add_carousel',
            'change_carousel',
            'delete_carousel',
            'view_carousel',
            'add_news',
            'change_news',
            'delete_news',
            'view_news',
            'add_program',
            'change_program',
            'delete_program',
            'view_program',
            'view_clubs',
            'change_clubs',
            'view_community',
            'change_community',
            ])
        
        permission_fest = Permission.objects.filter(codename__in=[
            'add_carousel',
            'change_carousel',
            'delete_carousel',
            'view_carousel',
            'add_news',
            'change_news',
            'delete_news',
            'view_news',
            'add_program',
            'change_program',
            'delete_program',
            'view_program',
            'view_fests',
            'change_fests',
            ])

        group_community.permissions.add(*permission_community)
        group_blood.permissions.add(*permission_blood)
        group_fest.permissions.add(*permission_fest)

        # creating default user for community,fest and bloodDonation

        #creating superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@gmail.com', 'pass')


        #creating bloodDonation user
        if not User.objects.filter(username='bloodDonation').exists():
            fest_user = User.objects.create_user('bloodDonation', 'bloodDonation@gmail.com', 'pass')
            fest_user.is_staff = True
            #adding to group community
            fest_user.groups.add(group_blood)
            fest_user.save()

        

