from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import TechConsultancyForm, TestimonialForm, AppointmentForm, BlogPost
from .forms import BlogPostForm


def home(request):
    return render(request, 'index.html')

def handle_form_submission(request, form_class, template_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank-you/')  # or any URL you want to redirect to
        else:
            return render(request, template_name, {'form': form})

    elif request.method == 'GET':
        form = form_class()
        return render(request, template_name, {'form': form})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def contact_form_view(request):
    return handle_form_submission(request, TechConsultancyForm, 'contact.html')

@csrf_exempt
def testimonial_form_view(request):
    return handle_form_submission(request, TestimonialForm, 'testimonials.html')

@csrf_exempt
def appointment_form_view(request):
    return handle_form_submission(request, AppointmentForm, 'appointment.html')

def blog_index(request):
    posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})

def blog_add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog_detail', post_id=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/add_post.html', {'form': form})

