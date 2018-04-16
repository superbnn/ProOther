from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from ProOther import settings
from app01.models import User


def index(request):
    '''进入首页'''
    return render(request, 'index.html')


def add_user(request):
    '''新增用户界面'''
    return render(request, 'add_user.html')


def do_add_user(request):
    '''新增用户操作'''
    #  获取上传的图片对象
    upload_file = request.FILES.get('avatar')
    upload_file = request.FILES.get('avatar')
    #  判断头像是否为空
    if not upload_file:
        return render(request, 'add_user.html', {'errmsg': '请选择用户头像'})
    file_name = upload_file.name
    file_path = settings.MEDIA_ROOT + "/app01/" + file_name
    #  将图片保存到服务器中
    with open(file_path, 'wb') as file:
        for data in upload_file.chunks():
            file.write(data)
    u = User()
    u.name = request.POST.get('name')
    u.avatar = '/app01/' + file_name
    u.save()
    return HttpResponse("新增用户成功")
    # return render(request, 'index.html')


def show_images(request):
    '''显示所有头像'''
    users = User.objects.all()
    context = {
        "users":users,
    }
    return render(request, 'show_images.html', context)