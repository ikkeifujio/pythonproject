from django.db import models
from django.db import models
# ユーザー認証
from django.contrib.auth.models import User
#時間
from django.utils import timezone
import random 
import datetime

#urlの末尾を同一にしないための関数
def random_url():
     chars = '0123456789abcdefghijkmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ'
     url = ''.join(random.choice(chars)for i in range(16))
     return url


#dbへデータを保存するためのクラス
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('タイトル',max_length=255)
    slug = models.SlugField(unique=True, default=random_url)
    intro = models.TextField()
    body = models.TextField('内容')
    posted_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
#調べる
class Account(models.Model):
    
    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    account_image = models.ImageField(upload_to="profile_pics",blank=True)
    def __str__(self):
        return self.user.username

class Schedule(models.Model):
    """スケジュール"""
    summary = models.CharField('概要', max_length=50)
    description = models.TextField('詳細な説明', blank=True)
    start_time = models.TimeField('開始時間', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('終了時間', default=datetime.time(7, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.summary


