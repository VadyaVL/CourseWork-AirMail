from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.shortcuts import redirect, render_to_response
from django.core.context_processors import csrf
from forms import *
from AirMail.views import updInformation, getInformation, getProfile
from models import *


def login(request):

    args = {}
    args['info'] = getInformation()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/auth/login/')

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserRegForm()
    args['info'] = getInformation()
    if request.POST:
        newUser_form = UserRegForm(request.POST)
        if newUser_form.is_valid():
            newUser_form.save()
            newUser = auth.authenticate(username=newUser_form.cleaned_data['username'], password=newUser_form.cleaned_data['password2'])
            auth.login(request, newUser)
            updInformation('cUser')
            return redirect('/')
        else:
            args['form'] = newUser_form
    return render_to_response('register.html', args)

def view(request):
    args = {}

    args['info'] = getInformation()
    args['user'] = request.user
    args['profile'] = getProfile(request.user)

    return render_to_response('aboutUser.html', args)

"""
def edit(request):
    args = {}
    args.update(csrf(request))

    args['info'] = getInformation()
    args['user'] = request.user
    args['form'] = UserRegForm(instance=request.user)

    return render_to_response('aboutUser.html', args)
    """