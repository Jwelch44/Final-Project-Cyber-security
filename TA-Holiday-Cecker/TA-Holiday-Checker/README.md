Holiday Checker
========================================

Holiday Checker contains a custom search command that will look at the date in an events _time field and will add a new field date_isholiday with a value that inidicates if the event's date occured on a holiday.

After installing this app, by copying it to $SPLUNK_HOME/etc/apps and restarting Splunk, you can run a search similar to the query below to determine if a given date is a holiday:


```
| makeresults count=365 | streamstats count | eval _time=_time-(count*24*60*60) | holidaycheck | table _time date_isholiday
```
Results:

_time| date_isholiday |
:-----|:-----|
2022-12-22 20:27:13 | 0 |
2022-12-23 20:27:13 | 0 |
2022-12-24 20:27:13 | 0 |
2022-12-25 20:27:13 | 1 |
2022-12-26 20:27:13 | 0 |

Note: Here _time value may vary per query, so date_isholiday value will change according to _time.

As an alternative to the above query, since it can have varing _time values you could run the following search to always get the results above:

```
| makeresults count=5 | streamstats count | eval _time=strptime("12/21/2022 20:27:13", "%m/%d/%Y %H:%M:%S") + (count*24*60*60) | holidaycheck | table _time date_isholiday
```


