#!/usr/bin/env python3

from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
import datetime
import holidays

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import dispatch, StreamingCommand, Configuration, Option, validators

@Configuration()
class StreamingHolidayCheck(StreamingCommand):
    """
    The holidaycheck command determines creates a new field date_isholiday based upon if _time is a holiday

    Example:

    ``| makeresults count=365 | streamstats count | eval _time=_time-(count*24*60*60) | holidaycheck``

    returns a record with one new field 'date_isholiday'.
    """

        def stream(self, records):
        for record in records:
            record['date_isholiday'] = 'holiday' if datetime.datetime.utcfromtimestamp(int(record['_time'])).date() in [ datetime.date(2021, 12, 31), \
            datetime.date(2022, 1, 17), datetime.date(2022, 2, 21), datetime.date(2022, 5, 30), datetime.date(2022, 6, 20), datetime.date(2022, 7, 4), \
            datetime.date(2022, 9, 5), datetime.date(2022, 10, 10), datetime.date(2022, 11, 11), datetime.date(2022, 11, 24), datetime.date(2022, 12, 26), \
                                                                                                                        
            datetime.date(2023, 1, 2), datetime.date(2023, 1, 16), datetime.date(2023, 2, 20), datetime.date(2023, 5, 29), datetime.date(2023, 6, 19), \
            datetime.date(2023, 7, 4), datetime.date(2023, 9, 4), datetime.date(2023, 10, 9), datetime.date(2023, 11, 11), datetime.date(2023, 11, 23), \
            datetime.date(2023, 12, 25) \ 

            datetime.date(2024, 1, 1), datetime.date(2024, 1, 15), datetime.date(2024, 2, 19), datetime.date(2024, 5, 27), datetime.date(2024, 6, 19), \
            datetime.date(2024, 7, 4), datetime.date(2024, 9, 2), datetime.date(2024, 10, 14), datetime.date(2024, 11, 11), datetime.date(2024, 11, 28), \
            datetime.date(2024, 12, 25)] \
            else 'none'
            yield record

dispatch(StreamingHolidayCheck, sys.argv, sys.stdin, sys.stdout, __name__)
