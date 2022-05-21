from django.urls import path
from app.views import GoalData, GoalDataUpdate, Login, Logout, AccountRegistration, bulletinboard, home, post_detail, MonthCalendar, MyCalendar, MonthWithFormsCalendar,MonthWithScheduleCalendar
GoalData,GoalDataUpdate
urlpatterns = [
    path('register/', AccountRegistration.as_view(), name='register'),
    path('login/', Login, name='login'),
    path("logout/", Logout, name="logout"),
    path("home/", home, name="home"),
    path("post_detail/<slug:slug>/", post_detail, name='post_detail'),
    path('mycalendar/', MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', MyCalendar.as_view(), name='mycalendar'
    ),
    path(
        'month_with_forms/',
        MonthWithFormsCalendar.as_view(), name='month_with_forms'
    ),
    path('month_with_forms/<int:year>/<int:month>/',MonthWithFormsCalendar.as_view(), name='month_with_forms'),
    path('bulletinboard/', bulletinboard, name="bulletinboard"),
    path('month/', MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/<int:day>/', MonthCalendar.as_view(), name='month'),
    path('month_with_schedule/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/<int:day>/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('goal_form/',GoalData.as_view() , name='goal_form'),
    path('goal_form/<int:year>/<int:month>/<int:day>/',GoalData.as_view(), name='goal_form'),
    path("goal_update/<int:pk>/", GoalDataUpdate.as_view(), name="goal_update")
]
