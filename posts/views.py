from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from .forms import PostCreateForm
from .models import Post, PostImage


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(FormView):
    form_class = PostCreateForm
    template_name = 'posts/create.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            post = Post(name=form.cleaned_data['title'])
            post.save()

            flag = True
            i = 0
            while(flag):
                key = 'file[%d]' % i
                f = request.FILES.get(key)
                if f is not None:
                    img = PostImage(post=post, img=f)
                    img.save()
                    i += 1
                else:
                    flag = False
            return HttpResponse(reverse('posts:detail', args=(post.id,)))
        else:
            return HttpResponse(reverse('posts:create'))
