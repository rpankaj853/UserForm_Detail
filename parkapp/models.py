from django.db import models
from datetime import datetime
#from django.contrib.auth.models import User

# Create your models here.

class parkmodel(models.Model):
	usrname = models.CharField(max_length =100)
	usremail = models.EmailField(max_length=254)
	usrnumber = models.IntegerField(blank=True, null=True)
	usrdob = models.DateTimeField(blank=False,null=False)



	def __str__(self):
		return self.usrname