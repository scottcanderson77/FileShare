# views.py
from django import forms
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User, Group

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )

            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response(
        'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):

    return render_to_response('home.html',{'user': request.user})

@csrf_exempt
def createGroup(request):
    if request.method == 'POST':
        user = request.user
        form = GroupForm(request.POST)
        group = form.instance
        if form.is_valid():

            form.save(commit=True)
            group.user_set.add(user)

        return HttpResponseRedirect('/allusers/')
    else:
        form = GroupForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'createGroup.html',
        variables,
    )



