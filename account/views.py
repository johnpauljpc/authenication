from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
#from django.urls import 

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
	return render(request, 'home.html')

class Signup(CreateView):
	form_class = UserCreationForm
	template_name = 'register.html'
	success_url = reverse_lazy('home')

def deposit(request):
	if request.method == 'POST':
		
		plan = int(request.POST.get('plan'))
		pla = request.POST.get('plan')
		print(type(plan))
		if plan == 1000:
			plan_name = 'One Month plan'
			messages.info(request, 'plan selected: ' + plan_name)
			
		elif plan == 2000:
			plan_name = "Two months plan"
			messages.info(request, 'plan selected:  ' + plan_name)
		
		context = {'plan': plan}
		#messages.info(request, "subscribed to  " + plan)
		return render(request, 'deposit/confirm.html', context)
	return render(request, 'deposit/deposit.html')