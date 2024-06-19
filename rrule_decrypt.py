from datetime import datetime
from dateutil import rrule, parser


def get_occurrences(rrule_string, dtstart_string):
    total = 0
    try:
        # Parse the DTSTART string
        dtstart = parser.parse(dtstart_string.split(':')[1])

        # Parse the recurrence rule string
        rule = rrule.rrulestr(rrule_string, dtstart=dtstart)

        # Get occurrences until today (as an aware datetime)
        now = datetime.now(dtstart.tzinfo)

        total = 0
        # Print each occurrence
        for occurrence in rule:
            if occurrence > now:
                break
            total += 1
            print(occurrence)
        print(total)

    except:
        print("Issue with " + str(rrule_string) + " at " + str(dtstart_string))



# Test:
get_occurrences('RRULE:FREQ=DAILY;BYHOUR=08;BYMINUTE=00;COUNT=3', 'DTSTART:20211118T120700Z')
