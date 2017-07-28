import time
import datetime

past = datetime.datetime.now()

time.sleep(5)

present = datetime.datetime.now()

time.sleep(5)

future = datetime.datetime.now()

print("Past {} > Present {}".format(past, present))
print( past > present)

print("Past {} < Future {}".format(past, future))
print( past < future)