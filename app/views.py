from django.shortcuts import render
from django.http import HttpResponse
from .assign1 import start

def scrape_data(request):
    city_list = [
    "Pune",
    "Delhi",
    "Mumbai",
    "Lucknow",
    "Agra",
    "Ahmedabad",
    "Kolkata",
    "Jaipur",
    "Chennai",
    "Bengaluru"
]

    for city in city_list:
        start(city) 

    return HttpResponse("Scraping completed.")
