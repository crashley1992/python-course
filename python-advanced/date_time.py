# lets you create objects for datetime/timezones
import datetime

mytime = datetime.time(2,20,1,20)
mytime.minute
mytime.hour
print(mytime)

mytime.microsecond

# have to use date oject to get date
today = datetime.date.today()
print(today)
today.year
today.month
today.day

# c time formatting
today.ctime() # gives back day(fri or mon) month day time year

from datetime import datetime
datetime(2020,10,3,14,20,1) 

# DATE  
from datetime import date
date1 = date(2021,11,3)
date2 = date(2020,11,3)

result = date1 - date2
type(result)
# might not take in leap year

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
print(datetime1 - datetime2)
