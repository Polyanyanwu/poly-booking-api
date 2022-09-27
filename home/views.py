from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    home_msg = "Welcome to our world"

    return render(request, 'home/index.html', {'msg': home_msg})
