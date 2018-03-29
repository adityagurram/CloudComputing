from django.shortcuts import render, redirect
from .forms import FibonacciGenerator

def Sequence_fibonacci(s_number):
    f_number=0
    sec_number = 1 
   # yield f_number
    for i in range(s_number):
        yield f_number+sec_number
        sec_number=f_number+sec_number
        f_number=sec_number-f_number

def get(request):
	form=FibonacciGenerator()		
	get_context={'form':form}	
	return render(request,'webapp/home.html', get_context)

def post(request):	
	form=FibonacciGenerator(request.POST)	
	if form.is_valid() or len(request.POST['inputNumber']) <3:
		form=FibonacciGenerator()
		input_known=str(request.POST['inputNumber'])
		given_input_number=int(input_known)		
		output=str(list(Sequence_fibonacci(given_input_number))).strip("[]")		
		post_context={'form':form,'output':output}	
				
	else:
		form=FibonacciGenerator()
		output="Please enter number between 1 to 100"		
		post_context={'form':form,'output':output}
	return render(request,'webapp/home.html',post_context)	









    





