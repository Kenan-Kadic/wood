from django.shortcuts import render

def homePageView(request):
    return render(request, 'pages/home.html')

def aboutPageView(request):
    return render(request, 'pages/about.html')

def financingPageView(request):
    return render(request, 'pages/financing.html')

def contactPageView(request):
    return render(request, 'pages/contact.html')

def exteriorPageView(request):
    return render(request, 'pages/exterior.html')

def interiorPageView(request):
    return render(request, 'pages/interior.html')

def areasWeServe(request):
    return render(request, 'pages/areasWeServe.html')

def kitchensPageView(request):
    return render(request, 'pages/kitchens.html')

def decksPageView(request):
    return render(request, 'pages/decks.html')

def fencingPageView(request):
    return render(request, 'pages/fencing.html')

def roofsPageView(request):
    return render(request, 'pages/roofs.html')

def sidingGutterPageView(request):
    return render(request, 'pages/sidinggutter.html')

def windowsDoorsPageView(request):
    return render(request, 'pages/windows_doors.html')

def bathroomsPageView(request):
    return render(request, 'pages/bathrooms.html')