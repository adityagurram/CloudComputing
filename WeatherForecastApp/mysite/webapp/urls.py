from django.conf.urls import url
from webapp import views
from webapp import viewsClimate
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
	url(r'^$',views.get,name="get"),
	]
urlpatterns = format_suffix_patterns(urlpatterns)