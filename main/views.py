from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View, ListView
from .forms import UserForm
from .models import Movie, Actor, ip
from django.contrib.auth import authenticate, login, logout
import datetime

def ip_addr(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ipaddress = x_forwarded_for.split(',')[-1].strip()
	else:
		ipaddress = request.META.get('REMOTE_ADDR')
		get_ip = ip() #imported class from model
		get_ip.ip_address= ipaddress
		get_ip.pub_date = datetime.date.today() #import datetime
		get_ip.save()
	
	return get_ip

class index(View):
	template_name = 'main/index.html'
	
	def get(self, request):
		form = Movie.objects.all()
		ip_addr(request)
		return render(request, self.template_name, {'object_list':form})
		
class UserFormView(View):
	form_class = UserForm
	template_name = 'main/registration.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})
	
	def post(self, request):
		form = self.form_class(request.POST)
		
		if form.is_valid():
		
			user = form.save(commit=False)
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user.set_password(password)
			user.save()

			# if Credential are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
		return render(request, self.template_name, {'form':form})

class LoginView(View):

	def get(self, request):
		ip_addr(request)
		return render(request, 'main/login.html')
	
	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('index')
		return render(request, 'main/login.html')
				
class LogoutView(View):

	def get(self, request):
		logout(request)
		return redirect('index')
		#return render(request, 'main/index.html')
		#return HttpResponseRedirect('main/index.html')