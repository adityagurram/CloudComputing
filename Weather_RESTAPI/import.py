import csv,sys,os

project_dir="C:/Users/adityagurram/Desktop/Django Tutorials/mysite"
sys.path.append(project_dir)
os.environ['DJANGO_SETTING_MODULE']='settings'


from webapp.models import Climate
data=csv.reader(open("C:/Users/adityagurram/Desktop/Django Tutorials/mysite/ClimateData.csv"),delimiter=",")

for row in data:
	if row[0]!='DATE':
		climate=Climate()
		climate.DATE=row[0]
		climate.TMAX=row[1]
		climate.TMIN=row[2]
		climate.save()
