from django.shortcuts import render
from .models import Account


# Create your views here.


def account(request):
    accounts = Account.objects.all()
    return render(request, 'webApp/bio.html', {'accounts': accounts})


def user_details(request, pk):
    detail = Account.objects.get(pk=pk)
    return render(request, 'webApp/userDetails.html', {'detail': detail})
