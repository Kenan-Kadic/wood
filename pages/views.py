from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class FinancingPageView(TemplateView):
    template_name = 'pages/financing.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class ExteriorPageView(TemplateView):
    template_name = 'pages/exterior.html'