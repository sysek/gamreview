from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin
from .models import Article


# Create your views here.

class HomeView(TemplateView):
    template_name = "articles/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['articles'] = Article.objects.all()
        return context


class ArticleListView(MultipleObjectMixin):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 2
    queryset = Article.objects.all()


class ArticleView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

