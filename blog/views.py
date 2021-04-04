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


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'    
    context_object_name = 'posts'
    paginate_by = 6    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content', 'privacy']

    def form_valid(self, forme):
        forme.instance.author = self.request.user
        return super().form_valid(forme)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'category', 'content', 'privacy']

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


def blog_by_category(request,cat):    
    return render(request,'blog/home.html',{'posts':Post.objects.filter(category=cat)})   

def about(request):
    print(Post.objects.filter(privacy='Private'))
    return render(request, 'blog/about.html', {'title': 'About'})  

def contact(request):
    if request.method == 'POST':
        formm = ContactUs(request.POST, instance=request.user)
        if formm.is_valid():
            formm.save()
            email = formm.cleaned_data.get('email')
            send_mail('Confirmation Email: Our Website', 'We Have got your Mail, We will contact you soon. ' , from_email=email, recipient_list=[email])
            messages.success(request, f'Successfully Submitted!')
            return redirect('blog-home') 

    else:
        formm = ContactUs(instance=request.user)

    context = {
        'formm': formm,
    }

    return render(request, 'blog/contact.html', context)        