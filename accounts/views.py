from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def SIGNIN(request):
	if (request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if (user == None):
			messages.error(request, 'Your username or password was incorrect.')
		else :
			login(request, user)
			if not (request.POST.get('remember-me', None)):
				request.session.set_expiry(0) # to prevent the user from getting saved
			return redirect('home:home')
	return render(request, './accounts/signin.html')

def SIGNOUT(request):
	logout(request)
	return redirect('home:home')

def SIGNUP(request):
	if (request.method == 'POST'):
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm-password']
		if not (password == confirm_password):
			messages.error(request, 'Your password dosen\'t match')

		else:
			if (User.objects.filter(username=username).exists()):
				messages.error(request, 'User already exists please sign in')

			else:
				if (len(password) < 8):
					messages.error(request, 'The length of your password must be of 8 characters or above')

				else:
					User.objects.create_user(username=username, password=password)
					user = authenticate(request, username=username, password=password)
					if (user == None):
						messages.error(request, 'An error occured please try again.')

					else :
						login(request, user)
						if not (request.POST.get('remember-me', None)):
							request.session.set_expiry(0)
						return redirect('home:home')
	return render(request, './accounts/signup.html')
