from django.shortcuts import render
from .models import Account


# Create your views here.


def account(request):
    accounts = Account.objects.all()
    # return render(request, 'webApp/user_list.html', {'accounts': accounts})
    return render(request, 'webApp/userList.html', {'accounts': accounts})


def user_details(request, pk):
    detail = Account.objects.get(pk=pk)
    return render(request, 'webApp/userDetails.html', {'detail': detail})
