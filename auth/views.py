from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout


def ulogin(request):
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

def ulogout(request):
    if request.user.is_authenticated():
      logout(request)
    return redirect('/login')
