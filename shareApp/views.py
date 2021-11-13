from django.conf import settings
from django.http import response
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import User, FileModel
from django.contrib.auth import login, authenticate, logout
import qrcode
from io import BytesIO
import os
from django.core.files import File
from PIL import Image, ImageDraw

def login_user(request):
    if request.method == 'POST':
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if user:
              login(request, user)  
              return redirect('home')
    return redirect("register")

def logout_user(request):
    logout(request)
    return redirect("login")


def detail(request, **args):
    file = FileModel.objects.get(id=args["pk"], user=request.user)
    user = request.user
    context = {
        "file": file,
        "user": user
    }
    return render(request, "shareApp/detail.html", context)


def create_qrcode(request):
    if request.is_ajax():
        file_inst = FileModel.objects.get(id=request.POST.get("id"), user=request.user)
        url_string = f"{request.META['HTTP_HOST']}/shareApp/filedownload/{request.user.username}/{file_inst.file_name}/{file_inst.id}"
        qrcode_img = qrcode.make(url_string)
        canvas = Image.new('RGB', (400,400), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f"{file_inst.file_name}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        file_inst.qrcode.save(fname, File(buffer), save=False)
        file_inst.save()
        return JsonResponse({"result":"ok"})  
    return HttpResponse("no itme")


def filedownload(request, **kwargs):
    file = FileModel.objects.get(id=kwargs["pk"])
    context = {"file": file}
    return render(request, "shareApp/downloadfile.html", context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response=HttpResponse(fh.read(), content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404