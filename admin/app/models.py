from django.db import models


# Create your models here.
class BookModel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, null=False)
    book_name = models.CharField(max_length=50)
    cover_url = models.CharField(max_length=50)
    description = models.TextField()
    last_chapter = models.CharField(max_length=50)
    class Meta():
        db_table = 'xwx_book'

class PhotoModel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, null=False)
    img_url = models.CharField(max_length=50)
    chapter_id = models.IntegerField()
    class Meta():
        db_table = 'xwx_photo'


class ChapterModel(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, null=False)
    chapter_name = models.CharField(max_length=50)
    book_id = models.IntegerField()
    img_url = models.CharField(max_length=255)
    class Meta():
        db_table = 'xwx_chapter'



class UserModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255, null=True)
    level = models.IntegerField(null=True)
    class Meta():
        db_table = 'xwx_user'

class BookShelfModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    book_id = models.IntegerField(null=True)
    create_time = models.IntegerField(null=True)
    update_time = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    iscollect = models.IntegerField(null=True)
    class Meta():
        db_table = 'xwx_user_book'

class CodeModel(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    phone = models.CharField(max_length=255, null=True)
    code = models.IntegerField(null=True)
    class Meta():
        db_table = 'xwx_smscode'