from django.shortcuts import redirect, render
from shareApp.forms import UserRegisterForm
from django.contrib.auth import login, authenticate



def home(request):
    return render(request, "base.html")

def dashboard(request):
    return render(request, "dashboard/index.html")

def register(request):
    context = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            context['form'] = form
    else:
        context['form'] = UserRegisterForm()        
        
    return render(request, "shareApp/register.html", context)