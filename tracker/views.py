from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views.generic import ListView
from tracker.models import Cryptocoin
import requests


# Create your views here.

def updatePopulateList():
    r = requests.get("https://api.coinmarketcap.com/v2/ticker/?limit=75")
    for key in r.json()['data']:
        try:
            obj, created = Cryptocoin.objects.update_or_create(rank=float(r.json()['data'][key]['rank']), defaults = {'name': r.json()['data'][key]['name'],
                                                                                                                     'image': "https://s2.coinmarketcap.com/static/img/coins/32x32/" + str(
                                                                                                                         r.json()['data'][key]['id']) + ".png",
                                                                                                                     'changehour': float(r.json()['data'][key]['quotes']['USD']['percent_change_1h']),
                                                                                                                     'changeday': float(r.json()['data'][key]['quotes']['USD']['percent_change_24h']),
                                                                                                                     'changeweek': float(r.json()['data'][key]['quotes']['USD']['percent_change_7d']),
                                                                                                                     'price': float(r.json()['data'][key]['quotes']['USD']['price']),
                                                                                                                     'cap': int(r.json()['data'][key]['quotes']['USD']['market_cap'])})
        except IntegrityError:
            print("EXISTS ALREADY")



class CryptocoinView(ListView):
    model = Cryptocoin
    updatePopulateList()

    def get_queryset(self):
        return Cryptocoin.objects.order_by('rank')


# Function to update list, calls function above on click
def reloadData(request):
    if request.method == "GET":
        updatePopulateList()
    return redirect('cryptocoin_list')
