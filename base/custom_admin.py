from django.contrib.admin import AdminSite,ModelAdmin
from .models import *
from django.utils.html import format_html


class bloodDonationAdminSite(AdminSite):
    site_header = 'Blood Donation Administration'
    site_title = 'Blood Donation Admin'
    index_title = 'Blood Donation Home'

    def has_permission(self, request):
        # Check if the user is logged in and is an active user
        if not request.user.is_active or not request.user.is_authenticated:
            return False
        # Check if the user belongs to the specific group
        return request.user.groups.filter(name='bloodDonation').exists()

class BloodDonationAdmin(ModelAdmin):
    list_display = ('name','blood_type', 'roll_no','course','phone_number_link')
    actions = ['add_to_donated']
    def phone_number_link(self, obj):
        # Format the phone number as a link
        phone_number = obj.phone
        link = f'<a href="tel:{phone_number}">{phone_number}</a>'
        return format_html(link)
    
    def add_to_donated(self, request, queryset):
        for obj in queryset:
            bloodDonated = BloodDonatedStudents()
            bloodDonated.name = obj.name
            bloodDonated.blood_type = obj.blood_type
            bloodDonated.roll_no = obj.roll_no
            bloodDonated.phone = obj.phone
            bloodDonated.save()
            obj.delete()

    add_to_donated.short_description = 'Add to Donated List'


class BloodDonatedStudentsAdmin(ModelAdmin):
    list_display = ('name','blood_type','roll_no','phone','donated_on')

blood_donation_admin_site = bloodDonationAdminSite(name='blood')
blood_donation_admin_site.register(BloodDonatedStudents, BloodDonatedStudentsAdmin)
blood_donation_admin_site.register(BloodDonation, BloodDonationAdmin)
blood_donation_admin_site.register(Bloodreq)








class CommunitiesAdminSite(AdminSite):
    site_header = 'Communities Administration'
    site_title = 'Communities Admin'
    index_title = 'Communities Home'

    def has_permission(self, request):
        # Check if the user is logged in and is an active user
        if not request.user.is_active or not request.user.is_authenticated:
            return False
        # Check if the user belongs to the specific group
        return request.user.groups.filter(name='community').exists()

    def each_context(self, request):
        context = super().each_context(request)
        user = request.user
        if user.is_authenticated:
            context['site_header'] = user.username  
        return context



class ProgramAdmin(ModelAdmin):
    list_display = ('name',)  
    exclude= ('created_by',)

    def save_model(self, request, obj, form, change):
        # Set the username of the user who created the instance
        obj.created_by = request.user.username
        # Save the instance
        super().save_model(request, obj, form, change)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(created_by=username)
        return qs


class NewsAdmin(ModelAdmin):
    list_display = ('title',)
    exclude= ('created_by',)  

    def save_model(self, request, obj, form, change):
        # Set the username of the user who created the instance
        obj.created_by = request.user.username

        # Save the instance
        super().save_model(request, obj, form, change)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(created_by=username)
        return qs

class CarouselAdmin(ModelAdmin):
    exclude= ('created_by',) 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'news':
            # Filter the queryset based on the current user
            kwargs['queryset'] = News.objects.filter(created_by__exact=request.user.username)
        elif db_field.name == 'program':
            # Filter the queryset based on the current user
            kwargs['queryset'] = Program.objects.filter(created_by__exact=request.user.username)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):
        # Set the username of the user who created the instance
        obj.created_by = request.user.username
        # Save the instance
        super().save_model(request, obj, form, change)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(created_by=username)
        return qs
    

class CommunityAdmin(ModelAdmin):
    list_display = ('name',) 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(name=username)
        return qs
    
class ClubAdmin(ModelAdmin):
    list_display = ('name',) 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(name=username)
        return qs

communities_admin_site = CommunitiesAdminSite(name='communities')

communities_admin_site.register(Program, ProgramAdmin)
communities_admin_site.register(News, NewsAdmin)
communities_admin_site.register(Community, CommunityAdmin)
communities_admin_site.register(Carousel, CarouselAdmin)
communities_admin_site.register(Clubs, ClubAdmin)






class FestAdminSite(AdminSite):
    site_header = 'Fests Administration'
    site_title = 'Fests Admin'
    index_title = 'Fests Home'


    def has_permission(self, request):
        # Check if the user is logged in and is an active user
        if not request.user.is_active or not request.user.is_authenticated:
            return False
        # Check if the user belongs to the specific group
        return request.user.groups.filter(name='fest').exists()

    def each_context(self, request):
        context = super().each_context(request)
        user = request.user
        if user.is_authenticated:
            context['site_header'] = user.username  
        return context
    

class FestsAdmin(ModelAdmin):
    list_display = ('name',) 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Apply filter to the queryset based on the name field
        username = request.user.username
        qs = qs.filter(name=username)
        return qs

fests_admin_site = FestAdminSite(name='fests')

fests_admin_site.register(Program, ProgramAdmin)
fests_admin_site.register(News, NewsAdmin)
fests_admin_site.register(Fests, FestsAdmin)
fests_admin_site.register(Carousel, CarouselAdmin)


