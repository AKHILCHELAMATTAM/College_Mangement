from django.http import HttpResponse

def student_home(request):
    return HttpResponse("Welcome to the Student section.")

