# from dateutil.rrule import *
# from dateutil.parser import *
# from datetime import *
#
# x = list(rrule(DAILY, count=10,dtstart=parse("19970902T090000")))
# print(x)
#
# # def chop(rr,sd):
# #     rr = rr.split(':')[1]
# #     rr = rr.split(';')
# #     print(rr)
# # chop("RRULE:FREQ=DAILY;BYHOUR=05;BYMINUTE=00;COUNT=1",1)
# RRULE:FREQ=DAILY;UNTIL=20210311T235900Z;BYHOUR=17;BYMINUTE=05;COUNT=1, DTSTART:20210310T170500Z
# RRULE:FREQ=DAILY;BYHOUR=09;BYMINUTE=10;COUNT=1, DTSTART:20210319T091000Z
from datetime import datetime
from dateutil import rrule, parser


def get_occurrences(rrule_string, dtstart_string):
    try:
        # Parse the DTSTART string
        dtstart = parser.parse(dtstart_string.split(':')[-1])

        # Parse the recurrence rule string
        rule = rrule.rrulestr(rrule_string, dtstart=dtstart)

        # Get occurrences until today (as an aware datetime)
        now = datetime.now(dtstart.tzinfo)
        occurrences = rule.before(now, inc=True)

        # Print each occurrence
        print("Occurrences of the event:")
        for occurrence in rule:
            if occurrence > now:
                break
            print(occurrence)

    except Exception as e:
        print(f"Error: {e}")



# Example usage with your inputs:
get_occurrences('RRULE:FREQ=DAILY;BYHOUR=08;BYMINUTE=00', 'DTSTART:20211118T120700Z')
