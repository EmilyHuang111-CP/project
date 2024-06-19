import cron_converter as cc
import datetime as dt
import constants as c
import calendar as cl

today = dt.datetime.now()

days_30 = today + dt.timedelta(days=-30, hours=0)

today = dt.datetime(2024, 1, 10, 10, 30, 00)

date_return = []

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


def handling_years(input_l):
    return input_l


def handling_question_marks(input_l):
    return str_cron.replace("?", "*")


def handling_hash_marks(input_l):
    global date_return
    if "#" in input_l:
        day_of_week = input_l.split(" ")[-1]
        day_week, time = day_of_week.split("#")
        print("ok")
        date_return = []
        for month in range(1, 13):
            days_in_month = []
            calendar_obj = cl.Calendar()
            for x in calendar_obj.itermonthdays4(today.year, month):
                # print(list(x))
                if list(x)[3] == (int(day_week) - 2) % 7 and list(x)[1] == month:
                    # print(x)
                    days_in_month.append(x)
                    # print("l", days_in_month)
                # print("f", days_in_month)
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


def handling_l(str_cron):
    str_cron.split()
    pass


def handling_year(str_cron):
    if len(str_cron.split(" ")) > 5:
        print("there's a year!")
    print(str_cron.replace(str_cron.split(" ")[-1], ""))
    return str_cron.replace(str_cron.split(" ")[-1], "")


def handling_w(str_cron):
    pass


def handling_slash(str_cron):
    pass


try:
    input_lst = "0 30 17 * 12 * 2008".strip()
    print(input_lst)
    str_cron = handling_seconds(input_lst)
    print(str_cron)
    str_cron = handling_years(str_cron)
    print(str_cron)
    str_cron = handling_question_marks(str_cron)
    print(str_cron)
    str_cron = handling_hash_marks(str_cron)
    print(str_cron)
    str_cron = handling_month_names(str_cron)
    print(str_cron)
    str_cron = handling_year(str_cron)
    cron_exp = cc.Cron(str_cron)
    # L
    # slashes
    # W

    dates = []

    # 0 30 9 * * 6#3
    # today.date() >
    date = today

    if "#" in str_cron:
        #while loop for as long as date is equal to or after start date
        for i in date_return:
            print(i)
            if today.date() > i > start_date.date():
                print(i)
                dates.append(i)
    else:
        while date > start_date:
            schedule = cron_exp.schedule(date)
            prev_date = schedule.prev()
            date = prev_date
            dates.append(date)

    print(len(dates), dates)

except Exception as E:
    print(E)
