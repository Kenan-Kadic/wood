from django.urls import path
from .views import homePageView, aboutPageView, financingPageView, contactPageView, exteriorPageView, interiorPageView, areasWeServe, kitchensPageView, decksPageView, fencingPageView, roofsPageView, sidingGutterPageView, windowsDoorsPageView,bathroomsPageView, atticInsulationPageView, workMidtownPageView, installMidtownPageView

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
    path('fencing/', fencingPageView, name='fencing'),
    path('roofs/', roofsPageView, name='roofs'),
    path('siding-gutter/', sidingGutterPageView, name='sideGutter'),
    path('windows-doors/', windowsDoorsPageView, name='windows_doors'),
    path('bathrooms/', bathroomsPageView, name='bathrooms'),
    path('attic-insulation/', atticInsulationPageView, name='attic_insulation'),
    path('work-at-midtown/', workMidtownPageView, name='work_midtown'),
    path('install-at-midtown/', installMidtownPageView, name='install_midtown'),
]
