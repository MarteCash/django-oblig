from django.conf.urls import petterns, include, url
from django.contrib import admin

from plls import views

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls'))
	url(r'^admin/', include(admin.site.urls))
)