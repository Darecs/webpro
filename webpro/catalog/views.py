from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@login_required
def dnac(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/dnac.html', context=context)

@login_required
def meraki(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/meraki.html', context=context)

@login_required
def iosxe(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/iosxe.html', context=context)

@login_required
def sdwan(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/sdwan.html', context=context)