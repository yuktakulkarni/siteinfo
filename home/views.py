from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def index(requests):
    return render(requests, 'index.html')


def login(requests):
    return HttpResponse("Login page")


def calc(requests):
    return render(requests, 'calc.html')


def contact(requests):
    return render(requests, 'contact copy.html')


def faq(requests):
    return render(requests, 'faq2.html')


def news(requests):
    return render(requests, 'news copy.html')


def subscribe(requests):
    return render(requests, 'subscribe.html')


def Bitocin(requests):
    return render(requests, 'Bitcoin.html')


def Ethereum(requests):
    return render(requests, 'Ethereum.html')


def XRP(requests):
    return render(requests, 'XRP.html')


def Cardano(requests):
    return render(requests, 'Cardano.html')


def Dogecoin(requests):
    return render(requests, 'Dogecoin.html')
