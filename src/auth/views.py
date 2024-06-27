from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    
    return render(request,'auth/login.html',{})
        # Redirect to a success page.
 

def register_view(request):
    return render(request, 'auth/login.html')
