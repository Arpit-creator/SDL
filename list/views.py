from django.shortcuts import render, redirect, get_object_or_404
from .models import todo_list, list_item
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def CREATE(request):
	if (request.method == 'POST'):
		if (request.POST.get('list-title', None)):
			todolist = todo_list.objects.create(user=request.user, heading=request.POST.get('list-title'))

		else:
			todolist = todo_list.objects.create(user=request.user)

	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def DELETE(request, pk):
	todolist = get_object_or_404(todo_list, pk=pk)
	todolist.delete()

	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def VIEW(request, pk):
	todolist = get_object_or_404(todo_list, pk=pk)
	items = list_item.objects.filter(item_of=todolist)
	if (request.user != todolist.user):
		raise Exception('You can\'t access someone else\'s list')
	context = {
		'list': todolist,
		'items_of_list': items,
	}
	return render(request, './list/view.html', context)

@login_required
def ADD(request, pk):
	if (request.method == 'POST'):
		todolist = get_object_or_404(todo_list, pk=pk)
		if (request.POST.get('item-value', None)):
			item = list_item.objects.create(item_of=todolist, value=request.POST.get('item-value'))

		else:
			item = list_item.objects.create(item_of=todolist)

	return redirect(request.META.get('HTTP_REFERER')) # takes us to the previous request

@login_required
def REMOVE(request, pk):
	item = get_object_or_404(list_item, pk=pk)
	item.delete()

	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def DONE(request, pk):
	item = get_object_or_404(list_item, pk=pk)
	if not(item.done):
		item.done = True
		item.save()

	return redirect(request.META.get('HTTP_REFERER'))
