from django.shortcuts import render
import requests
import datetime

# Create your views here.
def index(request):
	py_ab_I = [4503.4,5528,3630.7,5954.7,4090.9]
	py_bc_I = [16728,7948,7152.75,6123.92,2338.2]

	# [4587, 6463, 5591, 10286, 7914]
# [15971, 34783, 45722, 28583, 21874]

	ty_ab_I=[]
	ty_bc_I=[]

	''' extracting date time for start and end time data -> to capture limited data'''
	'''time=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%s')
	newtime_two= (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%s')'''
	time=(datetime.datetime.now() - datetime.timedelta(days=2)).replace(hour=18,minute=0,second=0).strftime('%s')
	newtime_two=(datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=6,minute=0,second=0).strftime('%s')

	############################################
	'''----------------Girls' hostel AB wing 0th floor------------'''
	gh_0_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/a2095480-eed6-584e-b5e4-d7199eee9ac3?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x0=gh_0_ab.content.split(',')[-1].split('\r')[0]
	y0=gh_0_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-0-ab starts:"
#	print
	ty_ab_I.append(int(float(x0)) - int(float(y0)))
#
#	print integer0
#	print "gh-0-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 1st floor------------'''
	gh_1_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/b7c99e66-e3be-596a-baf9-47b01f9e21f9?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x1=gh_1_ab.content.split(',')[-1].split('\r')[0]
	y1=gh_1_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-1-ab starts:"
#	print int(float(y1))
#	integer1=int(float(x1))
	ty_ab_I.append(int(float(x1)) - int(float(y1)))
#	print integer1
#	print "gh-1-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 2nd floor------------'''
	gh_2_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/d232a8a7-00f0-5260-95ff-5705899b2db4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x2=gh_2_ab.content.split(',')[-1].split('\r')[0]
	y2=gh_2_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-2-ab starts:"
#	print int(float(y2))
#	integer2=int(float(x2))
	ty_ab_I.append(int(float(x2)) - int(float(y2)))
#	print integer2
#	print "gh-2-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 3rd floor------------'''
	gh_3_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/c01563d5-e52e-5fcb-bd01-4fbe247ee2d4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x3=gh_3_ab.content.split(',')[-1].split('\r')[0]
	y3=gh_3_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-3-ab starts:"
#	print int(float(y3))
#	integer3=int(float(x3))
	ty_ab_I.append(int(float(x3)) - int(float(y3)))
#	print integer3
#	print "gh-3-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 4th floor------------'''
	gh_4_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/945e47fa-2e48-5b07-8771-6c84751a269c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x4=gh_4_ab.content.split(',')[-1].split('\r')[0]
	y4=gh_4_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-4-ab starts:"
#	print int(float(y4))
#	integer4=int(float(x4))
	ty_ab_I.append(int(float(x4)) - int(float(y4)))
#	print integer4
#	print "gh-4-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################

	'''----------------Girls' hostel BC wing 0th floor------------'''
	gh_0_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/5303e59f-33eb-57ea-a025-f85afce3316c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x00=gh_0_bc.content.split(',')[-1].split('\r')[0]
	y00=gh_0_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-0-bc starts:"
#	print int(float(y00))
#	integer00=int(float(x00))
	ty_bc_I.append(int(float(x00)) - int(float(y00)))
#	print integer00
#	print "gh-0-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 1st floor------------'''
	gh_1_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/82af7ba3-db7d-518a-97b6-eae47508d2d5?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x11=gh_1_bc.content.split(',')[-1].split('\r')[0]
	y11=gh_1_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
	ty_bc_I.append(int(float(x11)) - int(float(y11)))
	#xxxxxxxxxxx Girls' hostel BC wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 2nd floor------------'''
	gh_2_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/376413c8-0dd0-5191-a291-091636b45a01?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x22=gh_2_bc.content.split(',')[-1].split('\r')[0]
	y22=gh_2_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-2-bc starts:"
#	print int(float(y22))
#	integer22=int(float(x22))
	ty_bc_I.append(int(float(x22)) - int(float(y22)))
#	print integer22
#	print "gh-2-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 3rd floor------------'''
	gh_3_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/afb6540a-45e6-52ab-95c1-6f8e019dc85b?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x33=gh_3_bc.content.split(',')[-1].split('\r')[0]
	y33=gh_3_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-3-bc starts:"
#	print int(float(y33))
#	integer33=int(float(x33))
	ty_bc_I.append(int(float(x33)) - int(float(y33)))
#	print integer33
#	print "gh-3-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 4th floor------------'''
	gh_4_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/6f96f660-5745-5467-b9b2-2a9ce4ce6b34?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x44=gh_4_bc.content.split(',')[-1].split('\r')[0]
	y44=gh_4_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-4-bc starts:"
#	print int(float(y44))
#	integer44=int(float(x44))
	ty_bc_I.append(int(float(x44)) - int(float(y44)))
#	print integer44
#	print "gh-4-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''

	ratios = []
	wing_ratio = []
	for x in xrange(0,5):
		rat = (ty_ab_I[x] / py_ab_I[x]) -1
		wing_ratio.append(color(rat))

	ratios.append(wing_ratio)

	wing_ratio_f = []
	for x in xrange(0,5):
		rat = (ty_bc_I[x] / py_bc_I[x]) -1
		wing_ratio_f.append(color(rat))

	ratios.append(wing_ratio_f)
	print ratios

	context = {'ratios':ratios}
	return render(request, 'powerdown/index.html', context)


def index_night(request):
	py_ab_II = [6567.05,7213.55,4268.85,9015.5,4020.45]
	py_bc_II = [14605.5,12537.875,10309.0,8054.1875,2647.4375]


# [8906, 9080, 6169, 14784, 9061]
# [6471, 14916, 18627, 10845, 8282]

	ty_ab_II=[]
	ty_bc_II=[]

	#########################################
#	New
	#########################################

	''' extracting date time for start and end time data -> to capture limited data'''
	'''time=(datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%s')
	newtime_two= (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%s')'''
	time=(datetime.datetime.now() - datetime.timedelta(days=3)).replace(hour=6,minute=0,second=0).strftime('%s')
	newtime_two=(datetime.datetime.now() - datetime.timedelta(days=4)).replace(hour=18,minute=0,second=0).strftime('%s')

	############################################
	'''----------------Girls' hostel AB wing 0th floor------------'''
	gh_0_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/a2095480-eed6-584e-b5e4-d7199eee9ac3?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x0 = gh_0_ab.content.split(',')[-1].split('\r')[0]
	y0 = gh_0_ab.text.split(',')[2].split('\r')[0] #give last 6hrs power consumption
#	print "gh-0-ab starts:"
#	print
	ty_ab_II.append(int(float(x0)) - int(float(y0)))
#
#	print integer0
#	print "gh-0-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 1st floor------------'''
	gh_1_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/b7c99e66-e3be-596a-baf9-47b01f9e21f9?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x1=gh_1_ab.content.split(',')[-1].split('\r')[0]
	y1=gh_1_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-1-ab starts:"
#	print int(float(y1))
#	integer1=int(float(x1))
	ty_ab_II.append(int(float(x1)) - int(float(y1)))
#	print integer1
#	print "gh-1-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 2nd floor------------'''
	gh_2_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/d232a8a7-00f0-5260-95ff-5705899b2db4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x2=gh_2_ab.content.split(',')[-1].split('\r')[0]
	y2=gh_2_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-2-ab starts:"
#	print int(float(y2))
#	integer2=int(float(x2))
	ty_ab_II.append(int(float(x2)) - int(float(y2)))
#	print integer2
#	print "gh-2-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 3rd floor------------'''
	gh_3_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/c01563d5-e52e-5fcb-bd01-4fbe247ee2d4?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x3=gh_3_ab.content.split(',')[-1].split('\r')[0]
	y3=gh_3_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-3-ab starts:"
#	print int(float(y3))
#	integer3=int(float(x3))
	ty_ab_II.append(int(float(x3)) - int(float(y3)))
#	print integer3
#	print "gh-3-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel AB wing 4th floor------------'''
	gh_4_ab=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/945e47fa-2e48-5b07-8771-6c84751a269c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x4=gh_4_ab.content.split(',')[-1].split('\r')[0]
	y4=gh_4_ab.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-4-ab starts:"
#	print int(float(y4))
#	integer4=int(float(x4))
	ty_ab_II.append(int(float(x4)) - int(float(y4)))
#	print integer4
#	print "gh-4-ab end\n"
	#xxxxxxxxxxx Girls' hostel AB wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################

	'''----------------Girls' hostel BC wing 0th floor------------'''
	gh_0_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/5303e59f-33eb-57ea-a025-f85afce3316c?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x00=gh_0_bc.content.split(',')[-1].split('\r')[0]
	y00=gh_0_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-0-bc starts:"
#	print int(float(y00))
#	integer00=int(float(x00))
	ty_bc_II.append(int(float(x00)) - int(float(y00)))
#	print integer00
#	print "gh-0-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 0th floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 1st floor------------'''
	gh_1_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/82af7ba3-db7d-518a-97b6-eae47508d2d5?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x11=gh_1_bc.content.split(',')[-1].split('\r')[0]
	y11=gh_1_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
	ty_bc_II.append(int(float(x11)) - int(float(y11)))
	#xxxxxxxxxxx Girls' hostel BC wing 1st floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 2nd floor------------'''
	gh_2_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/376413c8-0dd0-5191-a291-091636b45a01?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x22=gh_2_bc.content.split(',')[-1].split('\r')[0]
	y22=gh_2_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-2-bc starts:"
#	print int(float(y22))
#	integer22=int(float(x22))
	ty_bc_II.append(int(float(x22)) - int(float(y22)))
#	print integer22
#	print "gh-2-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 2nd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 3rd floor------------'''
	gh_3_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/afb6540a-45e6-52ab-95c1-6f8e019dc85b?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x33=gh_3_bc.content.split(',')[-1].split('\r')[0]
	y33=gh_3_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-3-bc starts:"
#	print int(float(y33))
#	integer33=int(float(x33))
	ty_bc_II.append(int(float(x33)) - int(float(y33)))
#	print integer33
#	print "gh-3-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 3rd floor ends xxxxxxxxxxxxxxxxxxx'''

	#########################################
	'''----------------Girls' hostel BC wing 4th floor------------'''
	gh_4_bc=requests.get("http://energy.iiitd.edu.in:9102/backend/api/data/uuid/6f96f660-5745-5467-b9b2-2a9ce4ce6b34?starttime="+newtime_two+"000&endtime="+time+"000&format=csv&tags=&timefmt=iso8601&")


	x44=gh_4_bc.content.split(',')[-1].split('\r')[0]
	y44=gh_4_bc.text.split(',')[2].split('\r')[0]#give last 6hrs power consumption
#	print "gh-4-bc starts:"
#	print int(float(y44))
#	integer44=int(float(x44))
	ty_bc_II.append(int(float(x44)) - int(float(y44)))
#	print integer44
#	print "gh-4-bc end\n"
	#xxxxxxxxxxx Girls' hostel BC wing 4th floor ends xxxxxxxxxxxxxxxxxxx'''
	
	ratios = []
	wing_ratio = []
	for x in xrange(0,5):
		rat = (ty_ab_II[x] / py_ab_II[x]) -1
		wing_ratio.append(color(rat))
	ratios.append(wing_ratio)

	wing_ratio = []
	for x in xrange(0,5):
		rat = (ty_bc_II[x] / py_bc_II[x]) -1
		wing_ratio.append(color(rat))
	ratios.append(wing_ratio)

	context = {'ratios':ratios}
	return render(request, 'powerdown/index_night.html', context)

def stats(request):
	return render(request, 'powerdown/charts.html')

def color(x):
    if (x <= 0.0):
    	return 16711680
    if (x >= 1.0):
    	return 65280
    if (x < 0.5):
        return int(510 * x) << 8
    else:
        return int(510 * (1.0 - x)) << 16