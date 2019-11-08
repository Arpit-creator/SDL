from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from list.models import todo_list

# Create your views here.
def HOME(request):
	if (request.user.is_authenticated):
		return redirect('home:user')
	return render(request, './home/home.html')

@login_required
def USER(request):
	context = {
		'lists_of_user': todo_list.objects.filter(user=request.user),
	}
	return render(request, './home/user.html', context)
