from django import forms

class FibonacciGenerator(forms.Form):
	inputNumber=forms.CharField(max_length=2,widget=forms.TextInput(attrs={'class':'form-control','type':'number', 'placeholder':'Number'}))
	