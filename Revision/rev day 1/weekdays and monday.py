import numpy as np
start=input("Enter the start date: ")
end=input("Enter the end date: ")
days = np.busday_count(start, end)
print('Number of weekdays is:', days)
monday=np.busday_offset(start, 0, roll='forward', weekmask='Mon')
print('First Monday from the given start date is: ', monday)
