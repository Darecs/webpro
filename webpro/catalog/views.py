from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def dnac(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/dnac.html', context=context)

def meraki(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/meraki.html', context=context)

def iosxe(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/iosxe.html', context=context)

def sdwan(request):
    """View function for home page of site."""
    
    context = {
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'applications/sdwan.html', context=context)