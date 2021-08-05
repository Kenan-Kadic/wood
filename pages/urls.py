from django.urls import path

from .views import HomePageView, AboutPageView, FinancingPageView, ContactPageView, ExteriorPageView, InteriorPageView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('financing/', FinancingPageView.as_view(), name='financing'),
    path('contact-us/', ContactPageView.as_view(), name='contact'),
    path('exterior/', ExteriorPageView.as_view(), name='exterior'),
    path('interior/', InteriorPageView.as_view(), name='interior'),
]
