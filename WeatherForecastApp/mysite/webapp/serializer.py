from rest_framework import serializers
from webapp.models import Climate

class ClimateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Climate
		fields=('DATE',
				'TMAX',
				'TMIN')
		