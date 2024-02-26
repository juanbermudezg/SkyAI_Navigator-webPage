from django.shortcuts import render, redirect
from .forms import CreateNewUser
from .models import Users

# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        print("por if")
        return render(request, 'users/sign_up.html', {
            'form': CreateNewUser()
        })
    else:
        Users.objects.create(
            username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        return redirect('sign_in')

def sign_in(request):
    return render(request, 'users/sign_in.html')
def mainPage(request):
    return render(request, 'index.html')