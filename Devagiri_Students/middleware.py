from django.shortcuts import redirect
from django.urls import reverse


class RestrictStaffAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_staff and not request.user.is_superuser:
            print(request.user.username)
            if request.user.username == 'blood':
                return redirect(reverse('blood')) 
        return self.get_response(request)
