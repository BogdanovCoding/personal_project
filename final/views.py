from django.shortcuts import render, redirect, get_object_or_404
#REQUIRES PIP INSTALL REQUESTS
#I USED
#$sudo easy_install requests!!!
import requests


def welcome(request):
    return render(request, 'welcome.html')

def stocks(request, get_stock_quote=None):
    try:
        get_stock_quote = request.GET['get_stock_api']
        if len(get_stock_quote) == 0:
            get_stock_quote = None    
    except:
        get_stock_quote = None
    if get_stock_quote != None:
        _str=f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={get_stock_quote}&apikey=XCHVDYQTNAA3KJ7S'
        r = requests.get(url=_str)
        stock = r.json()
        try:
            get_stock_quote = f'Current price of {get_stock_quote} is : {stock["Global Quote"]["05. price"]}'
        except:
            get_stock_quote= None
    return render(request, 'stocks.html', {'get_stock_quote': get_stock_quote})

def forex(request):
    r = requests.get(url='http://data.fixer.io/api/latest?access_key=94d1bd52b528c201750f99c3b89a4181&symbols=GBP,JPY,USD,AUD')
    api_JSON = r.json()
    list_of_rates = []
    new_dict=api_JSON['rates']
    for key in new_dict:
        _temp_str = f'{key} : {new_dict[key]}'
        list_of_rates.append(_temp_str)
    forex_dict = {'forex_pairs':list_of_rates}
    return render(request, 'forex.html', forex_dict)

def crud(request):
    return render(request, 'crud.html')
