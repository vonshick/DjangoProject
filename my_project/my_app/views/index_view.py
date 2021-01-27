from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'my_app/index.html'

