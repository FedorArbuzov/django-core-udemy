from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    res = HttpResponse(content_type='text/html')
    res.content = '<h1>HELLO</h1>'
    res.status_code = 200
    return res

def redirect_somewhere(request):
    return HttpResponseRedirect('/')