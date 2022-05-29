from unittest import skip
from django.http import HttpRequest
import datetime
from .models import Goal
def some_processor(request: HttpRequest):
    year_month = []
    date = datetime.date.today()
    date = date.replace(year=date.year, month=date.month, day=1)
    year_month.append(date)
    context = {}
    context["year_month_day"] = year_month
    goal_all = Goal.objects.all()
    for i in range(0, len(goal_all)):
        goal_first = goal_all[i]
        context["goal_first"] = goal_first
        if 1 != goal_first:
            break
    # dic = create_dict()
    # return dic
    return context