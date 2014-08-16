from django.shortcuts import render

def index(request):
  if not request.user.is_authenticated():
    return redirect('/login')
  return render(request, 'users/index.html')

