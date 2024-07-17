from django.http import HttpResponse

def staff_home(request):
    return HttpResponse("Welcome to the Staff section.")

