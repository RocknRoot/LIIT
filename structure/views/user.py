from django.template import RequestContext
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response,redirect
from django.core.context_processors import csrf
from structure.forms import LIITRegistrationForm
from django.contrib.auth import authenticate, login, logout

def index(request):
  if not request.user.is_authenticated():
    return redirect('/login')
  return render(request, 'users/index.html')

def register(request):
  if request.user.is_authenticated():
    return redirect('/home')
  if request.method == 'POST':
    form = LIITRegistrationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return redirect('/login')
  else:
    form = LIITRegistrationForm()
  return render(request, 'users/register.html', {
    'form': form, })

def custom_login(request):
    state = "Please log in..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('/home')
            else:
                state = "Your account is inactive, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth/login.html', {'state': state, 'username': username},
                              context_instance=RequestContext(request))

def custom_logout(request):
    if request.user.is_authenticated():
      logout(request)
    return redirect('/login')
