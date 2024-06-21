import datetime as dt
from dateutil import rrule, parser


def get_occurrences(rrule_string, dtstart_string):
    total = 0
    try:
        # Parse the DTSTART string
        dtstart = parser.parse(dtstart_string.split(':')[1])

        # Parse the recurrence rule string
        rule = rrule.rrulestr(rrule_string, dtstart=dtstart)

        # Get occurrences until today (as an aware datetime)
        now = dt.datetime.now(dtstart.tzinfo)
        days_30 = now + dt.timedelta(days=-30, hours=0)

        total = 0
        # Print each occurrence
        for occurrence in rule:
            if occurrence > days_30:
                if occurrence > now:
                    break
                total += 1
                print(occurrence)
        print(total)

    except Exception as err:
        print("Error:" + str(err) +  "\nwith " + str(rrule_string) + " at " + str(dtstart_string))



# Test:
get_occurrences('RRULE:FREQ=MONTHLY;UNTIL=20250501T235900Z;BYMONTHDAY=01;BYHOUR=00;BYMINUTE=00','RT:20240115T090000Z')
