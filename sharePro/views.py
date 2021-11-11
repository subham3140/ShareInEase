from django.shortcuts import redirect, render
from shareApp.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from shareApp.models import FileModel, User
from django.http import JsonResponse


def home(request):
    return render(request, "base.html")

def dashboard(request):
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
    print(assignment)
   
    return render(request, "profile/index.html", context)