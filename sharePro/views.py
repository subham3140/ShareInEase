from django.shortcuts import redirect, render
from shareApp.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from shareApp.models import FileModel, User



def home(request):
    return render(request, "base.html")

def dashboard(request):
    files = FileModel.objects.filter(user=request.user)
    context = {
        "files": files
    }
    return render(request, "dashboard/index.html", context)

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


def profile(request):
    user = request.user
    context = { "user": user}
    return render(request, "profile/index.html", context)