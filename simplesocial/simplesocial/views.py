from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

# Homepage view using TemplateView in the project views
class HomePage(TemplateView):
    template_name = 'index.html'
