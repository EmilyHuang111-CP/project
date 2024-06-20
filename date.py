import cron_converter as cc
import datetime as dt
import constants as c
import calendar as cl

today = dt.datetime.now()

calendar_obj = cl.Calendar()

today = dt.datetime(2024, 1, 2, 10, 30, 00)

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
    if len(str_cron.split(" ")) > 5:
        print("there's a year!")
        years.append(str_cron.split(" ")[-1].split(","))
        str_cron = " ".join(str_cron.split(" ")[:-1])
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
            for x in cl.monthcalendar(today.year-1, month):
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



def handling_slash(str_cron):
    pass


# try:
input_lst = "0 23 7 2L * * 2023".strip()
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
cron_exp = cc.Cron(str_cron)
# L
# slashes
# W

dates = []

# 0 30 9 * * 6#3
# today.date() >
date = today

if "#" in input_lst or "L" in input_lst:
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
            if str(date.year) in years[0]:
                dates.append(date)
        else:
            dates.append(date)

print(len(dates), dates)

# except Exception as E:
#     print(E)
