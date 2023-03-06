from django.shortcuts import render, redirect
from .models import AccountDetails
from django.contrib.auth.decorators import login_required
from login.models import User


def indexview(request):
    return render(request, 'base/index.html')


@login_required(login_url='login:login')
def homepage(request):
    return render(request, 'base/homepage.html')


@login_required(login_url='login:login')
def addaccount(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        username = request.POST.get('username')
        password = request.POST.get('password')
        info = request.POST.get('info')

        account = AccountDetails(website=website, username=username, password=password, description=info,
                                 user=request.user)
        account.save()
        return redirect('base:view')
    return render(request, 'base/create.html')


@login_required(login_url='login:login')
def view(request):
    objects = AccountDetails.objects.all()
    context = {
        'objects': objects
    }
    return render(request, 'base/view.html', context)


@login_required(login_url='login:login')
def detailview(request, id):
    objects = AccountDetails.objects.get(id=id)
    if objects in request.user.accountdetails.all():
        context = {
            'objects': objects
        }

    else:
        return render(request, 'base/view.html', )
    return render(request, 'base/detailview.html', context)


@login_required(login_url='login:login')
def updateinfo(request, id):
    account = AccountDetails.objects.get(id=id)
    if request.method == 'POST':
        account.website = request.POST.get('website')
        account.username = request.POST.get('username')
        account.password = request.POST.get('password')
        account.description = request.POST.get('info')

        account.save()
        return redirect('base:detail', id=id)

    return render(request, 'base/create.html', {'account': account})


@login_required(login_url='login:login')
def deleteinfo(request, id):
    objects = AccountDetails.objects.get(id=id)
    context = {
        'objects': objects
    }
    if request.method == 'POST':
        objects.delete()
        return redirect('base:view')

    return render(request, 'base/delete.html', context)
