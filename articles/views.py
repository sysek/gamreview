from django.views.generic import TemplateView
from .models import Article


# Create your views here.

class HomeView(TemplateView):
    template_name = "articles/base.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['articles'] = Article.objects.order_by('-date')
        return context
