from django.shortcuts import render

def hod_home(request):
    return render(request, 'index.html')
