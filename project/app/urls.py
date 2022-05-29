from django.urls import path
from app.views import IndividualFormCalendar,GoalData, GoalMonthUpdate, GoalYearUpdate, Login, Logout, AccountRegistration, bulletinboard, home, post_detail, MonthCalendar, MyCalendar, MonthWithScheduleCalendar
GoalData,GoalMonthUpdate, GoalYearUpdate, 
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
    path('bulletinboard/', bulletinboard, name="bulletinboard"),
    path('month/', MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/<int:day>/', MonthCalendar.as_view(), name='month'),
    path('month_with_schedule/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('month_with_schedule/<int:year>/<int:month>/<int:day>/', MonthWithScheduleCalendar.as_view(), name='month_with_schedule'),
    path('goal_form/',GoalData.as_view() , name='goal_form'),
    path('goal_form/<int:year>/<int:month>/<int:day>/',GoalData.as_view(), name='goal_form'),
    path("goal_month_update/<int:pk>/<int:year>/<int:month>/<int:day>/", GoalMonthUpdate.as_view(), name="goal_month_update"),
    path("goal_year_update/<int:pk>/<int:year>/<int:month>/<int:day>/", GoalYearUpdate.as_view(), name="goal_year_update"),
    path('individual_calendar/', IndividualFormCalendar.as_view(), name='individual_calendar'),
    path('individual_calendar/<int:year>/<int:month>/<int:day>/', IndividualFormCalendar.as_view(), name='individual_calendar'),
]
