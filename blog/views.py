from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.mail import send_mail
from django.contrib import messages
from .models import Post
from .forms import ContactUs

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


class ExplorePostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['posts'] = Post.objects.filter(privacy='Public').exclude(author=self.request.user)
        else:
            context['posts'] = Post.objects.filter(privacy='Public')
        context['title'] = 'Explore'
        return context

    template_name = 'blog/all_post.html'
    ordering = ['-date_posted']
    paginate_by = 6
    
class MyblogPostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.request.user)
        context['title'] = 'My Blogs'
        return context

    template_name = 'blog/all_post.html'    
    ordering = ['-date_posted']
    paginate_by = 6

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'privacy']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Post'
        return context

    def form_valid(self, forme):
        forme.instance.author = self.request.user
        return super().form_valid(forme)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'content', 'privacy']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Post'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class blog_by_category(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(privacy='Public',category=self.kwargs['cat'])
        context['title'] = self.kwargs['cat'] + 'Blogs'
        return context

    template_name = 'blog/all_post.html'
    ordering = ['-date_posted']
    paginate_by = 6

def home(request):
    return render(request, 'blog/home.html',{'title':'Home'})  

def contact(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            formm = ContactUs(request.POST, instance=request.user)
        else:
            formm = ContactUs(request.POST)
        
        if formm.is_valid():
            formm.save()
            email = formm.cleaned_data.get('email')
            # send_mail('Confirmation Email: Our Website', 'We Have got your Mail, We will contact you soon.' , from_email=email, recipient_list=[email])
            send_mail('Confirmation Email: Our Website', 'We Have got your Mail, We will contact you soon. ', 'bakadiyayash@gmail.com', recipient_list=[email])
            messages.success(request, f'Successfully Submitted!')
            return redirect('blog-home') 

    else:
        if request.user.is_authenticated:
            formm = ContactUs(instance=request.user)
        else:
            formm = ContactUs()
    context = {
        'formm': formm,
        'title':'Contact'
    }

    return render(request, 'blog/contact.html', context)        