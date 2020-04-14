from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import catalog.dispatcher.dnac_api_dispatcher as dna
import json
from .models import dna_center

# Temp bis Authentifizierung ausgelagert wird
dna_login_token =  dna.dnac_login(dna.dnac["host"], dna.dnac["username"], dna.dnac["password"])

# Create your views here.
def index(request):
    """View function for home page of site."""
    
    context = {
        
    }
    return render(request, 'index.html', context=context)

@login_required
def dnac(request):
    """View function for home page of site."""
    context = {
        
    }
    return render(request, 'dnac_base.html', context=context)

@login_required
def dnac_login(request):
    """View function for home page of site."""

    
    context = {
        'dna_center': dna_center
    }
    return render(request, 'applications/dnac/dnac_login.html', context=context)

@login_required
def dnac_api1(request):
    """View function for home page of site."""

    device_list_raw = dna.network_device_list(dna.dnac, dna_login_token)
    device_list = device_list_raw["response"] 
    # print(device_list[0]["type"])
    context = {
        'device_list': device_list
    }
    return render(request, 'applications/dnac/dnac_api1.html', context=context)

@login_required
def dnac_api2(request):
    """View function for home page of site."""

    device_count = dna.device_count(dna.dnac, dna_login_token)
    context = {
        'device_count': device_count
    }
    return render(request, 'applications/dnac/dnac_api2.html', context=context)

@login_required
def meraki(request):
    """View function for home page of site."""
    
    context = {
        
    }
    return render(request, 'applications/meraki.html', context=context)

@login_required
def iosxe(request):
    """View function for home page of site."""
    
    context = {
        
    }
    return render(request, 'applications/iosxe.html', context=context)

@login_required
def sdwan(request):
    """View function for home page of site."""
    
    context = {
        
    }
    return render(request, 'applications/sdwan.html', context=context)