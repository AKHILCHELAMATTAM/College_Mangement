from django.http import HttpResponse

def hod_home(request):
    return HttpResponse("Welcome to the HOD section.")
