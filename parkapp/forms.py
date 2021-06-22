from django import forms
from .models import parkmodel


class parkform(forms.ModelForm):
	class Meta:

		model = parkmodel

		fields = ('usrname','usremail','usrnumber','usrdob')




