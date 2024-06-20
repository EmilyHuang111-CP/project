import cron_converter as cc
import datetime as dt
import constants as c
import calendar as cl

today = dt.datetime.now()

calendar_obj = cl.Calendar()

today = dt.datetime(2024, 1, 4, 10, 30, 00)

days_30 = today + dt.timedelta(days=-30, hours=0)

date_return = []

years = []

print("current", today)
print(days_30)

# event occurs every day at 9:30am
# started at 9am on June 2nd

start_date = dt.datetime(2008, 1, 2, 10, 30, 00)

if days_30 < start_date:
    pass
else:
    start_date = days_30


def handling_seconds(input_l):
    input_l = input_l.split(" ")[1:]
    input_str = " ".join(input_l)
    return input_str


def handling_question_marks(input_l):
    return str_cron.replace("?", "*")


def handling_hash_marks(input_l):
    global date_return, calendar_obj
    print("i", input_l)
    if "#" in input_l:
        print(input_l)
        day_of_week = input_l.split(" ")[-1]
        print("day", day_of_week)
        day_week, time = day_of_week.split("#")
        print("ok")
        date_return = []
        for month in range(1, 13):
            days_in_month = []
            for x in calendar_obj.itermonthdays4(today.year - 1, month):
                # print(list(x))
                if list(x)[3] == (int(day_week) - 2) % 7 and list(x)[1] == month:
                    days_in_month.append(x)
            for x in calendar_obj.itermonthdays4(today.year, month):
                # print(list(x))
                if list(x)[3] == (int(day_week) - 2) % 7 and list(x)[1] == month:
                    days_in_month.append(x)
            day_list = days_in_month[int(time)]
            date_return.append(dt.date(day_list[0], day_list[1], day_list[2]))
        print("dr", date_return)
        return input_l.replace(str(day_of_week), "*")
    else:
        return input_l


def handling_month_names(str_cron):
    for i in c.months:
        if i in str_cron:
            str_cron = str_cron.replace(i, str(c.months[i]))
    return str_cron


def handling_year(str_cron):
    split_cron = str_cron.split(" ")
    if len(split_cron) > 5:
        print("there's a year!")
        if "," in split_cron[-1]:
            split_cron2 = split_cron[-1].split(",")
            for x in split_cron2:
                print("x", x)
                if "-" in x:
                    print("x", x)
                    x = x.split("-")
                    print("x", x)
                    while int(x[0]) <= int(x[1]):
                        years.append(int(x[0]))
                        x[0] = int(x[0]) + 1
                else:
                    years.append(int(x))
            print("p", split_cron2)
        else:
            for x in split_cron:
                if "-" in x:
                    x = x.split("-")
                    while int(x[0]) <= int(x[1]):
                        years.append(x[0])
                        x[0] += 1
        str_cron = " ".join(split_cron[:-1])
    return str_cron


def handling_l(str_cron):
    global calendar_obj, date_return
    ss = str_cron.split(' ')
    if 'L' == ss[2]:
        for month in range(1, 13):
            date_return.append(dt.date(today.year, month, cl.monthrange(today.year, month)[1]))
            date_return.append(dt.date(today.year - 1, month, cl.monthrange(today.year - 1, month)[1]))
        return str_cron.replace("L", "*")
    elif 'L' in ss[2]:
        day_of_month = str_cron.split(" ")[-3]
        print("dm", day_of_month)
        print(date_return)
        weekdy, nothing = list(day_of_month)
        for month in range(1, 13):
            day = []
            for x in cl.monthcalendar(today.year - 1, month):
                print("pp", x)
                day.append(x[int((int(weekdy) - 2) % 7)])
            date_return.append(dt.date(today.year - 1, month, max(day)))
            for x in cl.monthcalendar(today.year, month):
                print("p", x)
                day.append(x[int((int(weekdy) - 2) % 7)])
            date_return.append(dt.date(today.year, month, max(day)))
        print("r", date_return)
        return str_cron.replace(day_of_month, "*")
    if 'L' in ss[4]:
        ss[4] = "7"
    return ' '.join(ss)


def handling_w(str_cron):
    w_use = str_cron.split(" ")[2]
    if 'W' in w_use:
        num = int(w_use[:-1])
        diffs = {}
        for month in range(1, 13):
            check_date = dt.date(year=today.year, month=month, day=num)
            days_2 = check_date + dt.timedelta(days=-2, hours=0)
            for i in range(5):
                if days_2.month == check_date.month and days_2.weekday() < 4:
                    diffs[abs(days_2.day - num)] = days_2
                days_2 += dt.timedelta(days=1, hours=0)
            date_return.append(diffs[min(list(diffs.keys()))])
            diffs = {}
        for month in range(1, 13):
            check_date = dt.date(year=today.year - 1, month=month, day=num)
            days_2 = check_date + dt.timedelta(days=-2, hours=0)
            for i in range(5):
                if days_2.month == check_date.month and days_2.weekday() < 4:
                    diffs[abs(days_2.day - num)] = days_2
                days_2 += dt.timedelta(days=1, hours=0)
            date_return.append(diffs[min(list(diffs.keys()))])
            diffs = {}
        return str_cron.replace(w_use, '*')

    else:
        return str_cron


def handling_slash(str_cron):
    parts = str_cron.split()
    new_parts = []
    position = 0

    for part in parts:
        if '/' in part:
            if part.startswith('*/'):
                step = int(part[2:])
                if step <= 0:
                    raise ValueError(f"Invalid step value '{step}' in cron expression.")

                if parts.index(part) == 0:  # Handling minutes
                    values = list(range(0, 60, step))
                elif parts.index(part) == 1:  # Handling hours
                    values = list(range(0, 24, step))
                elif parts.index(part) == 2:  # Handling days of month
                    values = list(range(1, 32, step))
                elif parts.index(part) == 3:  # Handling months
                    values = list(range(1, 13, step))
                elif parts.index(part) == 4:  # Handling days of week
                    values = list(range(0, 7, step))
                else:
                    raise ValueError(f"Unexpected position of '/' in cron expression.")

            else:
                position = part.index('/')
                start = part[:position]
                step = int(part[position + 1:])

                if start == '*':
                    start = 0
                else:
                    start = int(start)

                if parts.index(part) == 0:  # Handling minutes
                    max_value = 59
                elif parts.index(part) == 1:  # Handling hours
                    max_value = 23
                elif parts.index(part) == 2:  # Handling days of month
                    max_value = 31
                elif parts.index(part) == 3:  # Handling months
                    max_value = 12
                elif parts.index(part) == 4:  # Handling days of week
                    max_value = 6
                else:
                    raise ValueError(f"Unexpected position of '/' in cron expression.")

                values = []
                current = start
                while current <= max_value:
                    values.append(current)
                    current += step


try:
    input_lst = "0 23 */2 * * * 2023".strip()
    print("in", input_lst)
    str_cron = handling_seconds(input_lst)
    print("s", str_cron)
    str_cron = handling_question_marks(str_cron)
    print("q", str_cron)
    str_cron = handling_month_names(str_cron)
    print("m", str_cron)
    str_cron = handling_year(str_cron)
    print("y", years)
    str_cron = handling_hash_marks(str_cron)
    print("h", str_cron)
    str_cron = handling_l(str_cron)
    print("l", str_cron)
    str_cron = handling_w(str_cron)
    print("w", str_cron)
    str_cron = handling_slash(str_cron)
    print("/", str_cron)
    print("specialdates", date_return)
    cron_exp = cc.Cron(str_cron)
    # L
    # slashes
    # W

    dates = []

    # 0 30 9 * * 6#3
    # today.date() >
    date = today

    if "#" in input_lst or "L" in input_lst or "W" in input_lst:
        #while loop for as long as date is equal to or after start date
        for i in date_return:
            print("ii", i)
            if today.date() > i > start_date.date():
                print(i)
                dates.append(i)
    else:
        while date > start_date:
            print(date)
            print(date.year)
            print(years)
            schedule = cron_exp.schedule(date)
            prev_date = schedule.prev()
            date = prev_date
            if years:
                if int(date.year) in years:
                    dates.append(date)
            else:
                dates.append(date)

    print("dates", len(dates), dates)

except Exception as E:
    print(E)
