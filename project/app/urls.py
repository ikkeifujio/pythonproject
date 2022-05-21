from django.urls import path
from app.views import Login, Logout, AccountRegistration, frontpage, home, post_detail, MonthCalendar, MyCalendar, MonthWithFormsCalendar,MonthWithScheduleCalendar
urlpatterns = [
    path('register/', AccountRegistration.as_view(), name='register'),
    path('login/', Login, name='login'),
    path("logout/", Logout, name="logout"),
    path("home/", home, name="home"),
    path("<slug:slug>", post_detail, name="post_detail"),
    path('mycalendar/', MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'month_with_forms/',
        MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path('month_with_forms/<int:year>/<int:month>/',MonthWithFormsCalendar.as_view(), name='month_with_forms'),
    path('bulletinboard/', frontpage, name="bulletinboard"),
    path('month/', MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', MonthCalendar.as_view(), name='month'),
    path('month_schedule/', MonthWithScheduleCalendar.as_view(), name='month_schedule'),
]