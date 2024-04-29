import requests
from django.http import JsonResponse

from django.shortcuts import redirect
from ..utils import FetchSummoner

def save_summoner(request, summoner_name):
    if request.method == 'POST':
        print(request.POST)
        summoner = FetchSummoner(summoner_name)

        """
        if summoner:
            # You might want to redirect to a success page or the same page with a success message
            return redirect('some_success_url')
        else:
            # Handle errors or redirect to an error page
            return redirect('some_error_url')
        """
    # If someone navigates directly to the URL or something else goes wrong
    return redirect('home')
