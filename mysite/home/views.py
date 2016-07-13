from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse

# ...
def getHomePage(request):
    return HttpResponse("Test")