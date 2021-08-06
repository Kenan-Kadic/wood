from django.urls import path
from .views import homePageView, aboutPageView, financingPageView, contactPageView, exteriorPageView, interiorPageView, areasWeServe, kitchensPageView, decksPageView

app_name = 'pages'
urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('financing/', financingPageView, name='financing'),
    path('contact-us/', contactPageView, name='contact'),
    path('exterior/', exteriorPageView, name='exterior'),
    path('interior/', interiorPageView, name='interior'),
    path('areas-we-serve/', areasWeServe, name='areasweserve'),
    path('kitchens/', kitchensPageView, name='kitchens'),
    path('decks-underdecking/', decksPageView, name='decks'),
]
