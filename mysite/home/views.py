from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

# ...
def getHomePage(request):
    template = loader.get_template('home/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
	
def login(request):
	c = {}
	c.update(csrf(request))
	try:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			# the password verified for the user
			if user.is_active:
				return render_to_response("Valid", c)
			else:
				return render_to_response("Inactive", c)
		else:
			# the authentication system was unable to verify the username and password
			return render_to_response("Invalid", c)
	except (KeyError):
		return render_to_response("Invalid", c)