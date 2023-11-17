from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from .forms import CommentForm, ContactForm
from .models import Blog, Photo, Employees, Biography, Comment


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/index.html'
    context_object_name = 'blogs'
    ordering = ['-date_added']

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'Новый контакт'
            message = f'Имя: {form.cleaned_data["first_name"]}\n' \
                      f'Фамилия: {form.cleaned_data["last_name"]}\n' \
                      f'Email: {form.cleaned_data["email"]}\n' \
                      f'Сообщение: {form.cleaned_data["message"]}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.DEFAULT_FROM_EMAIL]

            send_mail(subject, message, from_email, recipient_list)

        return redirect('blog-list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['photos'] = Photo.objects.all()
        context['employees'] = Employees.objects.all()
        context['biography'] = Biography.objects.all()
        context['form'] = ContactForm()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blogs/single.html'
    context_object_name = 'blog'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

        return redirect(reverse('blog-detail', args=[self.kwargs['pk']]))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['form'] = CommentForm()
        return context
