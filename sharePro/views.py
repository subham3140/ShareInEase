from django.contrib.auth.backends import RemoteUserBackend
from django.http.response import FileResponse
from django.shortcuts import redirect, render
from shareApp.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from shareApp.models import FileModel, User
from django.http import JsonResponse
from PIL import Image
import os

def if_anonymous(func):
    def checkauthentication(*args, **kwargs):
        if not args[0].user.is_authenticated:
            return redirect("login")
        return func(*args, **kwargs)
    return checkauthentication



@if_anonymous
def home(request):
    return render(request, "base.html")

@if_anonymous
def dashboard(request):
    context = {}
    if request.is_ajax():
        result1 = [0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result2temp = {"assignment":0, "syllabus":0, "report": 0,"notice": 0, "result":0, "other": 0}
        try:
           files = FileModel.objects.filter(user=request.user)
           for file in files:
               result1[int(file.uploaded_at.month)-1] += 1
               result2temp[f"{file.file_type}"] += 1
        except:
           files = 0 
        result2 = [result2temp[item] for item in result2temp]
        return JsonResponse({"data1": result1, "data2":result2})
    files = FileModel.objects.filter(user=request.user).order_by("-uploaded_at")
    context = {
        "files": files,
        "user": User.objects.get(id=request.user.id)
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

@if_anonymous
def profile(request):
    user = request.user
    assignment = FileModel.objects.filter(user=user, file_type="assignment")
    syllabus = FileModel.objects.filter(user=user, file_type="syllabus")
    report = FileModel.objects.filter(user=user, file_type="report")
    notice = FileModel.objects.filter(user=user, file_type="notice")
    result = FileModel.objects.filter(user=user, file_type="result")
    other = FileModel.objects.filter(user=user, file_type="other")
    context = { 
        "user": user,
        "assignment": assignment,
        "syllabus": syllabus,
        "report": report,
        "notice": notice,
        "result": result,
        "other": other
        }
   
    return render(request, "profile/index.html", context)


@if_anonymous
def checkqrcode(request):
        if request.is_ajax():
            try:
               filemodel = FileModel.objects.get(id=request.GET.get("fileid"))
            except:
                return redirect("profile")            
            data = ""
            result = ""
            if filemodel.qrcode:
                result = "present"
                fn = filemodel.qrcode.path
                response = FileResponse(open(fn, 'rb'), content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="'+os.path.basename(fn)+'"'
                data = filemodel.qrcode.url
            else:
                result = "absent"
        return JsonResponse({"data": data, "result": result})



def aboutus(request):
    return render(request, "about.html")