from django.shortcuts import render

def handler404(request, *args, **argv):
    return render(request, './calc/404.html', status=404)