from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from webapp.serializer import ClimateSerializer
from webapp.models import Climate
from rest_framework.response import Response
from rest_framework.decorators import api_view

import csv
import datetime
import json

def load_climateData(request):
	data=csv.reader(open("C:/Users/adityagurram/Desktop/Django Tutorials/mysite/ClimateData.csv"),delimiter=",")
	for row in data:
		if row[0]!='DATE':
			climate=Climate()
			climate.DATE=row[0]
			climate.TMAX=row[1]
			climate.TMIN=row[2]
			climate.save()

@api_view(['GET', 'POST'])
def climate_list(request):
	if request.method=='GET':
		climates=Climate.objects.all()
		climate_serializer=ClimateSerializer(climates,many=True)
		data_list = []	
		for data in climate_serializer.data:
			date=data['DATE']
			Data_DATE={'DATE':date}
			data_list.append(Data_DATE)
		responseData=json.dumps(data_list)
		responseData=responseData.replace("\"", "").replace('"','')
		print(responseData)
		#return Response(climate_serializer.data)
		return Response(data_list)
	elif request.method=='POST':
		climate_data=JSONParser().parse(request)
		climate_serializer=ClimateSerializer(data=climate_data)
		if climate_serializer.is_valid():
			climate_serializer.save()
			responseData = { 'DATE' : climate_serializer.data['DATE'] }
			return Response(responseData,status=201)
		return Response(climate_serializer.errors,status=400)

@api_view(['GET', 'DELETE'])
def climate_detail(request,DATE):
	try:
		#Climate.objects.all().delete()
		climate=Climate.objects.get(DATE=DATE)
	except Climate.DoesNotExist:
		responseData="Bad Request - Data Not Exist"
		return Response(responseData,status=404)
	if request.method=='GET':
		climate_serializer=ClimateSerializer(climate)
		return Response(climate_serializer.data)
	elif request.method=='DELETE':
		climate.delete()
		responseData="No Content to Return"
		return Response(responseData,status=204)

@api_view(['GET'])
def climate_Forecast_Detail(request,DATE):
	if request.method=='GET':
		startDate=DATE	
		data_list = []	
		date_1 = datetime.datetime.strptime(startDate, "%Y%m%d")
		for x in range(1, 8):
			end_date = date_1 + datetime.timedelta(days=x)
			Req_date1=end_date.strftime('%Y%m%d')
			adding=int(str(Req_date1[-1]))			
			digits1 = [ int(char) for char in str(Req_date1) ]
			TMAX = sum( digits1 )
			Req_date2=end_date.strftime('%Y%m')
			digits2 = [ int(char) for char in str(Req_date2) ]
			if int(str(Req_date1[-2]))==0:
				TMIN=sum(digits2)/x
			else:
				TMIN = adding+(sum( digits2))/x
			data={'DATE': Req_date1, 'TMAX': TMAX, 'TMIN':TMIN}							
			data_list.append(data)				
		json_data =json.dumps(data_list)		
		json_data = json_data.replace("\"", "").replace('"',"")
	return Response(json_data)