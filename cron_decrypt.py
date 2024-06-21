import croniter as cr
import datetime as dt
years = []
w_list = []
now = dt.datetime.now()

def handling_question_marks(str_cron):
    return str_cron.replace("?", "*")

def handling_years(str_cron):
    global years
    check = 0
    split_cron = str_cron.split(' ')
    check_list = []
    for num in split_cron[-1]:
        if num == ',' or num == '-':
            if len(check_list) > 3:
                check = 1
                break
            else:
                check_list = []
        else:
            check_list.append(num)
    if len(check_list) > 3:
        check = 1
    if check == 1:
        print('hi')
        if "," in split_cron[-1]:
            split_cron2 = split_cron[-1].split(",")
            for x in split_cron2:
                if "-" in x:
                    x = x.split("-")
                    while int(x[0]) <= int(x[1]):
                        years.append(int(x[0]))
                        x[0] = int(x[0]) + 1
                else:
                    years.append(int(x))
        else:
            x = split_cron[-1]
            if "-" in x:
                x = x.split("-")
                while int(x[0]) <= int(x[1]):
                    years.append(int(x[0]))
                    x[0] = int(x[0]) + 1
            else:
                years.append(int(x))
        str_cron = " ".join(split_cron[:-1])
    #This will not work if there is nothign entered for seconds but something for years since years is optional and seconds aren't
    if len(split_cron) > 6 and split_cron[-1] == '*':
        str_cron = " ".join(split_cron[:-1])
    return str_cron

def handling_seconds(str_cron):
    split_cron = str_cron.split(' ')
    if len(split_cron) > 5:
        seconds = split_cron[0]
        split_cron.pop(0)
        split_cron.append(seconds)
        str_cron = " ".join(split_cron)
    return str_cron


def handling_l(str_cron):
    split_cron = str_cron.split(' ')
    if split_cron[4] == '1':
        split_cron[4] = 'SUN'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '2':
        split_cron[4] = 'MON'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '3':
        split_cron[4] = 'TUE'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '4':
        split_cron[4] = 'WED'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '5':
        split_cron[4] = 'THU'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '6':
        split_cron[4] = 'FRI'
        str_cron = " ".join(split_cron)
    elif split_cron[4] == '7' or split_cron[4] == '0' or split_cron[4] == 'L':
        split_cron[4] = 'SAT'
        str_cron = " ".join(split_cron)
    return str_cron


def handling_w(str_cron):
    w_use = str_cron.split(" ")[2]
    if 'W' in w_use:
        num = int(w_use[:-1])
        diffs = {}
        for month in range(1, 13):
            check_date = dt.date(year=now.year, month=month, day=num)
            days_2 = check_date + dt.timedelta(days=-2, hours=0)
            for i in range(5):
                if days_2.month == check_date.month and days_2.weekday() < 4:
                    diffs[abs(days_2.day - num)] = days_2
                days_2 += dt.timedelta(days=1, hours=0)
            w_list.append(diffs[min(list(diffs.keys()))])
            diffs = {}
        for month in range(1, 13):
            check_date = dt.date(year=now.year - 1, month=month, day=num)
            days_2 = check_date + dt.timedelta(days=-2, hours=0)
            for i in range(5):
                if days_2.month == check_date.month and days_2.weekday() < 4:
                    diffs[abs(days_2.day - num)] = days_2
                days_2 += dt.timedelta(days=1, hours=0)
            w_list.append(diffs[min(list(diffs.keys()))])
            diffs = {}
    return str_cron.replace(w_use, '*')


def count_cron_occurrences(str_cron):
    days_30 = now + dt.timedelta(days=-30, hours=0)

    first_occurrence = cr.croniter(str_cron, days_30)
    occurrences = []
    count = 0

    while True:
        next_date = first_occurrence.get_next(dt.datetime)
        if next_date > now:
            break
        if next_date >= days_30:
            if len(years) > 0:
                if len(w_list) != 0:
                    if next_date.year in years and next_date.date() in w_list:
                        occurrences.append(next_date)
                        count += 1
                else:
                    if next_date.year in years:
                        occurrences.append(next_date)
                        count += 1
            else:
                if len(w_list) != 0:
                    if next_date.date() in w_list:
                        occurrences.append(next_date)
                        count += 1
                else:
                    occurrences.append(next_date)
                    count += 1

    print(f"Occurrences in the last 30 days ({days_30.date()} to {now.date()}):")
    for occurrence in occurrences:
        print(occurrence)

    print(f"Total number of occurrences in the last 30 days: {count}")


# Example usage:
str_cron = '0/30 30 */3 13W * ? 2024'  # Example cron expression (every 15 minutes) # 12 1 1 *
print(str_cron, "OG")
str_cron = handling_question_marks(str_cron)
print(str_cron, "Question marks handled")
str_cron = handling_years(str_cron)
print(str_cron, "Years handled")
str_cron = handling_seconds(str_cron)
print(str_cron, "Seconds handled")
str_cron = handling_l(str_cron)
print(str_cron, "L handled")
str_cron = handling_w(str_cron)
print(str_cron, "W handled")
count_cron_occurrences(str_cron)
