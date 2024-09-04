from django.http import HttpResponse,JsonResponse
import requests
import json
from django.shortcuts import render

def home(request):
    return render(request, "form.html")

def movie_poster(request):

    movie_name = request.GET['search']

    print(movie_name)
    print(type(movie_name))

    response = requests.get(f'http://www.omdbapi.com/?&apikey=33e2608&s={movie_name}')
    response = response.json()
    print(response)
    

    if 'Search' in response and len(response['Search']) > 0:
        # Safely access the first poster (or the 6th if you prefer)
        poster_url = response['Search']
    else:
        # Fallback image if no results or an error occurred
        return HttpResponse("<h1>No Such Movie Found</h1>")

    content = {'Poster_url' : poster_url}

    
    return render(request, 'index.html', content)

    
