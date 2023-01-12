import datetime
from django.shortcuts import render, Http404, redirect

# Create your views here.


# def month_view(request, year, month_number):
#     if month_number < 1 or month_number > 12:
#         raise Http404('Miesiąc o takim numerze nie istnieje')
#     actual_date = datetime.date.today()
#     days = []
#     for i in range(1, 32):
#         try:
#             tmp = datetime.date(year, month_number, i)
#         except ValueError:
#             break
#         else:
#             days.append(tmp)
#
#     next_month = month_number + 1
#     next_year = year
#     if next_month > 12:
#         next_month = 1
#         next_year += 1
#     prev_month = month_number - 1
#     prev_year = year
#     if prev_month < 1:
#         prev_month = 12
#         prev_year -= 1
#
#     ctx = {'today': actual_date, 'days': days, 'prev': prev_month, 'next': next_month, 'next_year': next_year,
#            'prev_year': prev_year}
#
#     return render(request, 'mycallendar/month.html', ctx)


def month_view(request, year, month_number):
    if month_number < 1 or month_number > 12:
        raise Http404('Miesiąc o takim numerze nie istnieje')
    actual_date = datetime.date.today()
    days = []
    for i in range(1, 32):
        try:
            tmp = datetime.date(year, month_number, i)
        except ValueError:
            break
        else:
            days.append(tmp)


    month = []
    week = []
    day_week = 1
    for day in days:
        for week_day in range(day_week, 8):
            if day.isoweekday() == week_day:
                week.append(day)
                day_week += 1
                if day == days[-1]:
                    continue
                else:
                    break
            else:
                week.append(None)
                day_week += 1
        if len(week) >= 7:
            day_week = 1
            month.append(week.copy())
            week.clear()

    next_month = month_number + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1
    prev_month = month_number - 1
    prev_year = year
    if prev_month < 1:
        prev_month = 12
        prev_year -= 1


    ctx = {'today': actual_date, 'days': days, 'prev': prev_month, 'next': next_month, 'next_year': next_year,
           'prev_year': prev_year, 'days_month': month}

    return render(request, 'mycallendar/month.html', ctx)


def show_current_month(request):
    actual_month = datetime.date.today()
    return redirect('calendar_month', month_number=actual_month.month, year=actual_month.year)
