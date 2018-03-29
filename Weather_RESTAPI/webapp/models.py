from django.db import models

class Climate(models.Model):
	DATE= models.IntegerField(unique=True)
	TMAX= models.FloatField(null=True, blank=True, default=None,)
	TMIN=models.FloatField(null=True, blank=True, default=None)
