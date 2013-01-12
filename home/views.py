from django.template import Context, loader
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def topmenu(request):
  elements = (
      ('/', _('Home')),
  )
  return elements

def index(request):
  t = loader.get_template('home/index.html')
  c = Context({
    'menu': topmenu(request)
  })
  return HttpResponse(t.render(c))
