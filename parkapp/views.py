import requests
from django.shortcuts import render, redirect

from .forms import parkform

from .models import parkmodel
from datetime import date
# Create your views here.
todays_date = date.today()

def index(request):
	parkms = parkmodel.objects.all()

	if request.method == 'POST':	
	
		parkf = parkform(request.POST)

		if parkf.is_valid():
			urdob= parkf.cleaned_data['usrdob']
			num = parkf.cleaned_data['usrnumber']

			num = len(str(num))

			tar = str(urdob)[0:4]
			

			if  todays_date.year - int(tar) >= 18 and int(num) == 10 :

				parkf.save()
				return redirect('formlist')

			else:
				parkf = parkform()


	else:
		parkf = parkform()

	



	context = {'parkf':parkf,'parkms':parkms}
	return render(request, 'parkzap/index.html',context)




def formlist(request):

	parkms = parkmodel.objects.all()


	return render(request,'parkzap/formlist.html',{

		'parkms':parkms,

		})
