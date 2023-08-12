from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # New URL pattern for the root URL
    path('contact/', views.contact_form_view, name='contact_form'),
    path('testimonials/', views.testimonial_form_view, name='testimonial_form'),
    path('appointment/', views.appointment_form_view, name='appointment_form'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('blog/add/', views.blog_add_post, name='blog_add_post'),
]
