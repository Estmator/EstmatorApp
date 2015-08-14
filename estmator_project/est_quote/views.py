from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed

@login_required
def quote_view(request):
    if request.method == 'POST':
        print request.POST
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(['POST'])
