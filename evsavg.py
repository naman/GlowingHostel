import requests
import datetime
# values list will store values at one instant for previous 10 days
values=[]

# we are finding prev day(10 days ) values at that hour/time of the day to get benchmark to compare the current values
for i in range(1,11):
	
	timeb4=(datetime.datetime.now()-datetime.timedelta(days=i)-datetime.timedelta(days=12)).strftime('%s')
	timeafter=(datetime.datetime.now()-datetime.timedelta(days=i)).strftime('%s')

	valueAt=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/d232a8a7-00f0-5260-95ff-5705899b2db4?starttime="+timeb4+"000&endtime="+timeafter+"000&format=csv&tags=&timefmt=iso8601&")
	text0=valueAt.text.split(',')[-1].split('\r')[0]#getting instant data of the ith day(according to loop)
	text1=valueAt.text.split(',')[-20].split('\r')[0]#getting instant data of the ith day(according to loop)
	integer0=int(float(text0)) # converting string to integer
	integer1=int(float(text1))
	values.append(integer0-integer1) 

#averaging the values in the list
avg=reduce(lambda x,y:x+y, values)/len(values)
print avg
print values





