from django.views import generic

from .models import Blog, Photo, Employees, Biography


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blogs/index.html'
    context_object_name = 'blogs'
    ordering = ['-date_added']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BlogListView, self).get_context_data()
        context['photos'] = Photo.objects.all()
        context['employees'] = Employees.objects.all()
        context['biography'] = Biography.objects.all()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blogs/single.html'
    context_object_name = 'blog'
