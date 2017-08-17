import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import ensure_csrf_cookie

from simpleapi.models import Data

@ensure_csrf_cookie
def index(request):
    return HttpResponse(loader.get_template('simpleapi/index.html').render({},
        request))

@ensure_csrf_cookie
def state(request):
    return HttpResponse(loader.get_template('simpleapi/state.html').render({},
        request))

def uploadText(request):
    if request.method != 'POST':
        return HttpResponse(status=400)
    try:
        data = json.loads(request.body, encoding='utf-8')
    except json.JSONDecodeError:
        return HttpResponse(status=406)
    txt = data.get('txt', uploadText)
    if txt is uploadText:
        return HttpResponse(status=424)
    if isinstance(txt, str):
        Data(txt=txt).save()
        return HttpResponse(status=200)
    return HttpResponse(status=428)

def getText(request):
    return JsonResponse([{'txt': t.txt} for t in Data.objects.all()],
        safe=False)
