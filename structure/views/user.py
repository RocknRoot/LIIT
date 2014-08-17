from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from structure.forms import LIITRegistrationForm

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
