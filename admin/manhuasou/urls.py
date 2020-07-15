"""manhuasou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app.views import showBookList,showChapterList,showPhotoList,search,getKeyword,register,get_user_all,login,change_pass,forgive_pass,collectBook,showBookShelf,showBookShelfList,imgToBase,sendSms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('showBooklist/<int:id>/<int:page>', showBookList),
    path('showChapterlist/<int:id>/<str:token>', showChapterList),
    path('showChapterlist/<int:id>/', showChapterList),
    path('showPhotolist/<int:id>/<str:token>', showPhotoList),
    path('search/<str:book_name>', search),
    path('getKeyword/<str:keyword>', getKeyword),
    path('register/<str:username>/<str:password>/<int:code>', register),
    path('get_user_all/', get_user_all),
    path('login/<str:username>/<str:password>', login),
    path('change_pass/<str:username>/<str:password>/<str:new_pass>', change_pass),
    path('forgive_pass/<str:email>', forgive_pass),
    path('collectBook/<int:book_id>/<str:token>/<int:iscollect>',collectBook),
    path('showBookShelf/<int:book_id>/<str:token>',showBookShelf),
    path('showBookShelfList/<str:token>',showBookShelfList),
    path('imgToBase', imgToBase),
    path('sendSms/<str:phone>',sendSms),

]
