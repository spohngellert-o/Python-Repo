from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth

# ...
def getHomePage(request):
    template = loader.get_template('home/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
	
def login(request):
	c = {}
	c.update(csrf(request))
	user = authenticate(username=request.POST.get('username', ''), password=request.POST.get('password', ''))
	if user is not None:
		# the password verified for the user
		auth.login(request, user)
		return HttpResponseRedirect("/polls")
	else:
		# the authentication system was unable to verify the username and password
		return render_to_response("home/failure.html", c)