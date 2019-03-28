from django.views.generic import TemplateView, DetailView
from .models import Article


# Create your views here.

class HomeView(TemplateView):
    template_name = "articles/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['articles'] = Article.objects.all()
        return context


class ArticleView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data()
        context['art'] = Article.objects.all()
        return context
