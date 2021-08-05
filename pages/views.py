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

