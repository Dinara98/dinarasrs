from django.shortcuts import render

# Create your views here.
from .models import Menu, Guest, Eating

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_menus=Menu.objects.all().count()
  
    # Available menus (status = 'a')
   
    num_guests=Guest.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_menus':num_menus,'num_guests':num_guests},
    )

from django.views import generic

class MenuListView(generic.ListView):
    model = Menu
    paginate_by = 2
class MenuDetailView(generic.DetailView):
    model = Menu