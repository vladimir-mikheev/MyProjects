from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import NewsFilter
from .forms import NewsForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.views import View
from .utils import send_article_email

class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object.category
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_news'
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if 'news' in self.request.path:
            post_type = 'NE'
        elif 'article' in self.request.path:
            post_type = 'AR'
        self.object.post_type = post_type
        self.object.save()
        # Отправка уведомления о новой новости
        send_article_email(self.object)
        return super().form_valid(form)



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.change_news'
    form_class = NewsForm
    model = News
    template_name = 'news_edit.html'


class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_news'
    model = News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(NewsList):
    model = News
    ordering = 'name'
    template_name = 'news_search.html'
    context_object_name = 'news_search'
    paginate_by = 10

class SubscribeCategoryView(View):
    def post(self, request, *args, **kwargs):
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        user = request.user
        category.subscribers.add(user)
        return redirect('news_list')