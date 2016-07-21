app_name = 'home'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getHomePage, name='home'),
	url(r'^home/$', views.login, name='login')
]