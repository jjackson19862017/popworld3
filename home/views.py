from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Display an index page
    """
    return render(request, "home.html")