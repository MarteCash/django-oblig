from django.conf.urls import petterns, include, url
from django.contrib import admin

from plls import views

urlpatterns = patterns('',
	url(r'^polls/', include('polls.urls'))
	url(r'^admin/', include(admin.site.urls))
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>/d+)/vote/$', views.vote, name='vote'),
)