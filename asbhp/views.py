from django.shortcuts import render

def Start(request):
    return render(request, 'start.html', {})
