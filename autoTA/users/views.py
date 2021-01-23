from django.shortcuts import render

# Create your views here.
def LoginView(request):
    return render(request, "login.html")

def SuccessView(request):
    return render(request, "success.html")
