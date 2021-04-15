from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About Page')

def contact(request):
    return HttpResponse('Contact Page')

def address(request):
    return HttpResponse('Address Page')

def technology(request):
    return HttpResponse('Technology Page')

def web(request):
    return HttpResponse('Web Page')

def mobile(request):
    return HttpResponse('Mobile Page')

def desktop(request):
    return HttpResponse('Desktop Page')