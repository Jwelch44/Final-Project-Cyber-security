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
            record['date_isholiday'] = datetime.datetime.utcfromtimestamp(int(record['time'])).date() in holidays.US(years=2022).keys()
            yield record

dispatch(StreamingHolidayCheck, sys.argv, sys.stdin, sys.stdout, __name__)
