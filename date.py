import datetime as dt

today = dt.datetime.now()

days_30 = today + dt.timedelta(days=-30, hours=0)

print("current", today)
print(days_30)

# event occurs every day at 9:30am
# started at 9am on June 2nd

start_date = dt.datetime(2024, 6, 2, 10, 30, 00)


if days_30 < start_date:
    start_date = start
else:
    start_date = days_30

