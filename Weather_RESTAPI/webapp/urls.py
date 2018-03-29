from django.conf.urls import url
from webapp import viewsClimate
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[	
	url(r'^historical/(?P<DATE>[0-9]+)/$',viewsClimate.climate_detail,name="ClimateDetail"),	
	url(r'^historical/$',viewsClimate.climate_list, name="ClimateList")	,	
	url(r'^load/',viewsClimate.load_climateData,name="loadClimateData"),
	url(r'^forecast/(?P<DATE>[0-9]+)/$',viewsClimate.climate_Forecast_Detail,name="Forecast")		
	]
urlpatterns = format_suffix_patterns(urlpatterns)
