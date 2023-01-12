import datetime

def month_view(year, month_number):
    if month_number < 1 or month_number > 12:
        raise ValueError('Miesiąc o takim numerze nie istnieje')
    actual_date = datetime.date.today()
    days = []
    for i in range(1, 32):
        try:
            tmp = datetime.date(year, month_number, i)
        except ValueError:
            break
        else:
            days.append(tmp)

    return days

# print(month_view(2023, 1))
days = month_view(2023, 1)
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



print(month)