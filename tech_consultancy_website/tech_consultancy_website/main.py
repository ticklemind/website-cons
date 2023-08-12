"""
## main.py

This file contains the main entry point for the Django application.

"""

import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .views import contact_form_view, testimonial_form_view, appointment_form_view

# Configure Django settings
settings.configure()

# Define URL patterns
urlpatterns = [
    path('contact', csrf_exempt(contact_form_view), name='contact_form'),
    path('testimonials', csrf_exempt(testimonial_form_view), name='testimonial_form'),
    path('appointment', csrf_exempt(appointment_form_view), name='appointment_form'),
]

# Get the WSGI application
application = get_wsgi_application()

# Define the index view
def index(request):
    return JsonResponse({'message': 'Welcome to the Tech Consultancy website!'})

# Execute the Django application
if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
