import datetime
from datetime import datetime
# import time

# print(time.ctime())
# print(datetime.datetime.now())
c=datetime.now()
# print(c)
# d=datetime.strftime(c," %Y/%m/%d  %H:%M:%S")
# d=datetime.strftime( c ,f"hour:min:sec , date-mont-year  [ %H:%M:%S , %d-%m-%Y ]")
d=datetime.strftime( c ,f"[ %H:%M:%S , %d-%m-%Y ]")
print(d)