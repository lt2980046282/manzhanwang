import base64
import json
import random
import time

import requests
from django.core import serializers
from django.http import HttpResponse

from app.models import BookModel, ChapterModel, PhotoModel, UserModel, BookShelfModel,CodeModel
import hashlib


# Create your views here.

def showBookList(request, id, page):
    queryset = BookModel.objects.all()
    book_list = serializers.serialize('json', queryset[id:page])
    return HttpResponse(book_list)


def showChapterList(request, id, token='any'):
    model = UserModel.objects.filter(token=token, level=1)
    print(model)
    if model:
        queryset = ChapterModel.objects.filter(book_id=id)
        book_list = serializers.serialize('json', queryset)
        return HttpResponse(book_list)
    else:
        queryset = ChapterModel.objects.filter(book_id=id)
        ls = []
        for i in queryset:
            data = {
                'pk': i.pk,
                'fields': {
                    'chapter_name': i.chapter_name,
                    'book_id': i.book_id,
                    'img_url': i.img_url
                },
                'isShow': False,
            }
            ls.append(data)
        return HttpResponse(json.dumps(ls))


def showPhotoList(request, id, token):
    model = UserModel.objects.filter(token=token, level=1)
    print(model)
    if model:
        queryset = PhotoModel.objects.filter(chapter_id=id)
        book_list = serializers.serialize('json', queryset)
        return HttpResponse(book_list)
    else:
        status = {
            'code': 400,
            'name': '你的权限不够！'
        }
        return HttpResponse(status)


def search(request, book_name):
    queryset = BookModel.objects.filter(book_name__icontains=book_name)
    book_list = serializers.serialize('json', queryset)
    return HttpResponse(book_list)


def getKeyword(request, keyword):
    queryset = BookModel.objects.filter(book_name__icontains=keyword)
    book_list = serializers.serialize('json', queryset)
    return HttpResponse(book_list)


def register(request, username, password, code):
    codemodel = CodeModel.objects.filter(code=code,phone=username)
    if codemodel:
        usermodel = UserModel.objects.values('username').filter(username=username)
        if usermodel:
            status = {
                'code': 100,
                'name': '用户名存在'
            }
        else:
            usermodel = UserModel()
            usermodel.username = username
            m = hashlib.md5(password.encode(encoding='utf8'))
            usermodel.password = m.hexdigest()
            username = username.encode("utf-8")
            token = base64.b64encode(username)
            usermodel.token = str(token, encoding='utf-8')
            usermodel.save()
            status = {
                'code': 101,
                'name': '注册成功'
            }
    else:
        status = {
            'code': 103,
            'name': '验证码不正确'
        }

    return HttpResponse(json.dumps(status))


def get_user_all(request):
    usermodel = UserModel.objects.all()
    json = serializers.serialize('json', usermodel)
    return HttpResponse(json)


def login(request, username, password):
    usermodel = UserModel.objects.values('username').filter(username=username)
    if usermodel:
        m = hashlib.md5(password.encode(encoding='utf8'))
        password = m.hexdigest()
        usermodel = UserModel.objects.values('username', 'token').filter(username=username, password=password)

        if usermodel:
            status = {
                'code': 201,
                'name': '登录成功',
                'token': usermodel[0]['token'],
            }
        else:
            status = {
                'code': 200,
                'name': '密码不正确'
            }
    else:
        status = {
            'code': 102,
            'name': '用户名不存在'
        }
    return HttpResponse(json.dumps(status))


def forgive_pass(requsest, email):
    usermodel = UserModel.objects.values('username').filter(email=email)
    if usermodel:
        status = {
            'code': 100,
            'name': '用户名存在'
        }
    return HttpResponse(json.dumps(status))


def change_pass(request, username, password, new_pass):
    m = hashlib.md5(password.encode(encoding='utf8'))
    password = m.hexdigest()
    usermodel = UserModel.objects.values('id').filter(username=username, password=password)
    if usermodel:
        m = hashlib.md5(new_pass.encode(encoding='utf8'))
        new_pass = m.hexdigest()
        UserModel.objects.filter(id=usermodel[0]['id']).update(password=new_pass)
        status = {
            'code': 301,
            'name': '修改成功'
        }
    else:
        status = {
            'code': 300,
            'name': '原密码不正确'
        }
    return HttpResponse(json.dumps(status))


def collectBook(request, book_id, token, iscollect):
    model = UserModel.objects.values('id').filter(token=token)
    if model:
        id = model[0]['id'],
        user_id = int(id[0])
        shelfmodel = BookShelfModel.objects.filter(user_id=user_id, book_id=book_id)
        if shelfmodel:
            BookShelfModel.objects.filter(user_id=user_id, book_id=book_id).update(update_time=time.time(),
                                                                                   iscollect=iscollect)
        else:
            bookselmodel = BookShelfModel()
            bookselmodel.book_id = book_id
            bookselmodel.user_id = user_id
            bookselmodel.create_time = time.time()
            bookselmodel.iscollect = 1
            bookselmodel.save()
    else:
        status = {
            'code': 400,
            'name': '你的权限不够！'
        }
        return HttpResponse(status)


def showBookShelf(requests, book_id, token):
    model = UserModel.objects.values('id').filter(token=token)
    if model:
        id = model[0]['id'],
        user_id = int(id[0])
        shelfmodel = BookShelfModel.objects.filter(user_id=user_id, book_id=book_id)
        data = shelfmodel[0].iscollect,
    else:
        data = {
            'code': 400,
            'name': '你的权限不够！'
        }
    return HttpResponse(json.dumps(data))


def showBookShelfList(requests, token):
    model = UserModel.objects.get(token=token)
    id = model.id,
    user_id = id[0]
    ls = []
    if model:
        bookmodels = BookModel.objects.raw(f'select * from xwx_book where id in (select book_id from xwx_user_book where user_id={user_id} and iscollect=1)')
        book_list = serializers.serialize('json', bookmodels[:])
        return HttpResponse(book_list)
    else:
        data = {
            'code': 400,
            'name': '你的权限不够！'
        }
        return HttpResponse(json.dumps(data))

def imgToBase(request):
    url = request.GET.get('url')
    data = requests.get(url).content
    base64_data = base64.b64encode(data)
    s = base64_data.decode()
    return HttpResponse('data:image/jpeg;base64,%s' % s)

def sendSms(request,phone):
    account = "I23543356"
    # 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
    password = "6185c681a4ecdb3bdc84d95870f7f2e2"
    mobile = f"86 {phone}"
    code = random.randint(100000, 999999)
    text = f"您的验证码是：{code}。请不要把验证码泄露给其他人。"
    data = {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'}
    url = 'http://api.isms.ihuyi.com/webservice/isms.php?method=Submit'
    res = requests.post(url, data)
    model =CodeModel()
    model.code = code
    model.phone = phone
    model.save()
    print(res.content)
    return HttpResponse(json.dumps(str(res.content,encoding='utf-8')))



