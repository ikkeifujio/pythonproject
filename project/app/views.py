from calendar import month
from curses import A_ALTCHARSET
from re import A
from tkinter import S
from appscript import k
from django.shortcuts import render, redirect
#テンプレートタグ(調べる)
from django.views.generic import TemplateView
from sympy import Id
from app.forms import ComentForm, PostForm, SimpleScheduleForm
from .models import Post
#ユーザーアカウントフォーム
from .forms import AccountForm, AddAccountForm

#ログイン、ログアウト時に必要
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views import generic
from . import mixins
from .forms import BS4ScheduleForm
from .models import Schedule
import datetime

#ログイン
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'blog/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('frontpage'))

#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "blog/home.html",context=params)

def frontpage(request):
    posts = Post.objects.all()
    user = request.user
    if request.method == "POST":
        post_forms = PostForm(request.POST)
        if post_forms.is_valid():
            posts2 = post_forms.save(commit=False)
            #ログインしているユーザーの名前を追加する
            posts2.user = request.user
            posts2.post = posts
            posts2.save()
            return redirect("bulletinboard")
    else:
        post_forms = PostForm()
        return render(request, "blog/bulletinboard.html", {"posts": posts, "post_forms":post_forms})

    return render(request, "blog/bulletinboard.html", {"posts": posts, "post_forms": post_forms, "user":user})

class frontpages(mixins.WeekWithScheduleMixin, generic.CreateView):
    template_name = 'blog/frontpage.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        context.update(week_calendar_context)
        posts = Post.objects.all()
        context["posts"] = posts
        post_forms = PostForm(self.request.GET or None)
        context.update({"post_forms":post_forms})
        return context

    def form_valid(self, form):
        post_forms = PostForm(self.request.POST)
        if post_forms.is_valid():
            posts2 = post_forms.save(commit=False)
            posts2.save()
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('frontpage', year=date.year, month=date.month, day=date.day)



def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = ComentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=post.slug)
    
    else:
        form = ComentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})


#アカウント作成(調べる)
class  AccountRegistration(TemplateView):
    
    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"blog/register.html",context=self.params)

    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"blog/register.html",context=self.params)




class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'blog/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context



class MyCalendar(mixins.MonthCalendarMixin, mixins.WeekWithScheduleMixin, generic.CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'blog/mycalendar.html'
    model = Schedule
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        print(date)
        schedule.save()
        return redirect('mycalendar', year=date.year, month=date.month, day=date.day)


class MonthWithFormsCalendar(mixins.MonthWithFormsMixin, generic.View):
    """フォーム付きの月間カレンダーを表示するビュー"""
    template_name = 'blog/month_with_forms.html'
    model = Schedule
    date_field = 'date'
    form_class = SimpleScheduleForm

    def get(self, request, **kwargs):
        context = self.get_month_calendar()
        return render(request, self.template_name, context)


    def post(self, request, **kwargs):
        context = self.get_month_calendar()
        formset = context['month_formset']
        if formset.is_valid():
            formset.save()
            return redirect('month_with_forms')

        return render(request, self.template_name, context)



class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView):
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'blog/month_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context