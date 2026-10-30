from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            message = "Login details validated successfully."
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form, "message": message})
