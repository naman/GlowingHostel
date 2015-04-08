import requests
import datetime

''' extracting date time for start and end time data -> to capture limited data'''
time=(datetime.datetime.now()-datetime.timedelta(seconds=2)).strftime('%s')
newtime_two= (datetime.datetime.now() - datetime.timedelta(minutes=60)).strftime('%s')
############################################
'''----------------Girls' hostel AB wing 0th floor------------'''
gh_0_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/a2095480-eed6-584e-b5e4-d7199eee9ac3?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


x0=gh_0_ab.content.split(',')[-1].split('\r')[0]
y0=gh_0_ab.text.split(',')[-20].split('\r')[0]#give last 10 min consumption
print "gh-0-ab starts:"
print int(float(y0))
integer0=int(float(x0))
#printing instant value in integer
print integer0
print "gh-0-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''

#########################################
'''----------------Girls' hostel AB wing 1st floor------------'''
gh_1_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/b7c99e66-e3be-596a-baf9-47b01f9e21f9?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


x1=gh_1_ab.content.split(',')[-1].split('\r')[0]
y1=gh_1_ab.text.split(',')[-20].split('\r')[0]
print "gh-1-ab starts:"
print int(float(y1))
integer1=int(float(x1))
#printing instant value in integer
print integer1
print "gh-1-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''

###############################################3
'''----------------Girls' hostel AB wing 2nd floor------------'''
gh_2_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/d232a8a7-00f0-5260-95ff-5705899b2db4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


x2=gh_2_ab.content.split(',')[-1].split('\r')[0]
y2=gh_2_ab.text.split(',')[-20].split('\r')[0]
print "gh-2-ab starts:"
print int(float(y2))
integer2=int(float(x2))
#printing instant value in integer
print integer2
print "gh-2-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''
###################################################

'''----------------Girls' hostel AB wing 3rd floor------------'''
gh_3_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/c01563d5-e52e-5fcb-bd01-4fbe247ee2d4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


x3=gh_3_ab.content.split(',')[-1].split('\r')[0]
y3=gh_3_ab.text.split(',')[-20].split('\r')[0]
print "gh-3-ab starts:"
print int(float(y3))
integer3=int(float(x3))
#printing instant value in integer
print integer3
print "gh-2-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''

####################################################3

'''----------------Girls' hostel AB wing 4th floor------------'''
gh_4_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/945e47fa-2e48-5b07-8771-6c84751a269c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


x4=gh_4_ab.content.split(',')[-1].split('\r')[0]
y4=gh_4_ab.text.split(',')[-20].split('\r')[0]
print "gh-4-ab starts:"
print int(float(y4))
integer4=int(float(x4))
#printing instant value in integer
print integer4
print "gh-4-ab end\n"
'''xxxxxxxxxxx Girls' hostel AB wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''

##################################################


