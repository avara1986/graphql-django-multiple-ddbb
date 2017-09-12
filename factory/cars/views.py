from django.http import HttpResponse
# Create your views here.


def index(request):
    html = "<html><body>The IP is %s.</body></html>" % request.META['REMOTE_ADDR']
    return HttpResponse(html)
