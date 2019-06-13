from django.views.generic import TemplateView, DetailView, ListView
from .models import Article


# Create your views here.

class HomeView(ListView):
    template_name = "articles/base.html"
    queryset = Article.objects.all()
    paginate_by = 5


class ArticleView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

