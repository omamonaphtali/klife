from django.shortcuts import render_to_response


# Create your views here.
def index(request):
    return render_to_response('index.html')


def contact(request):
    return render_to_response('contact.html')


def gallery(request):
    return render_to_response('gallery.html')
