## models.py
from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class TechConsultancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    expertise = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)


class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField()


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField()
    message = models.TextField()


class TechConsultancyForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


class TestimonialForm(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)


class AppointmentForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateTimeField()
    message = models.TextField()
