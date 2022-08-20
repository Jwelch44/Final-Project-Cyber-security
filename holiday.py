#!/usr/bin/env python

import holidays # This is the pip holiday list
import datetime # Importing datetime module
from datetime import date # Importing date class from datetime module
import sys # This is for splunk custom commands
import os # This is for splunk custom commands
import time;  # This is required to include time module.




sys.path.insert(0, os.path.join(os.path.dirname(Holidaycheck.py), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, ReportingCommand, Configuration, Option, validators

# Select country
us_holidays = holidays.US()
today = date.today()

@Configuration()
class HolidayCommand(ReportingCommand):

    @Configuration()
    def map(self, events):
        # Put your streaming preop implementation here, or remove the map method,
        # if you have no need for a streaming preop

	#Loop over the events
	for event in events:
		# Read the _time field since that has the events timestamp
		# Eventually it would be great to make this configurable, but they can
		# always manipulate the _time in SPL 
		event_date_time = event['_time']
		
		#Call your function and save it to a new field
		#Save the result in a field called date_is_holiday
		# Again it would be great to make this configurable
		event['date_is_holiday'] = foo(event_date_time)

    def reduce(self, events):
        # Put your reporting implementation
        pass

dispatch(%(command.title())Command, sys.argv, sys.stdin, sys.stdout, __name__)
