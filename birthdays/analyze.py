# Stat 302 Project 2 Data collection spider.
# Crawling http://www.foxsports.com/mlb/players pages 1 through 116 for birthday information
# Copyright Evan Kivolowitz
# 11/20/16

import matplotlib.pyplot as plt




months = {
	"Jan" : 0,
	"Feb" : 0,
	"Mar" : 0,
	"Apr" : 0,
	"May" : 0,
	"Jun" : 0,
	"Jul" : 0,
	"Aug" : 0,
	"Sep" : 0,
	"Oct" : 0,
	"Nov" : 0,
	"Dec" : 0
}


with open("birthdays.txt", 'r') as f:
	for line in f:
		month = int(line.split("/")[0])
		if month == 1:
			months["Jan"] = months["Jan"] + 1
		elif month == 2:
			months["Feb"] = months["Feb"] + 1
		elif month == 3:
			months["Mar"] = months["Mar"] + 1
		elif month == 4:
			months["Apr"] = months["Apr"] + 1
		elif month == 5:
			months["May"] = months["May"] + 1
		elif month == 6:
			months["Jun"] = months["Jun"] + 1
		elif month == 7:
			months["Jul"] = months["Jul"] + 1
		elif month == 8:
			months["Aug"] = months["Aug"] + 1
		elif month == 9:
			months["Sep"] = months["Sep"] + 1
		elif month == 10:
			months["Oct"] = months["Oct"] + 1
		elif month == 11:
			months["Nov"] = months["Nov"] + 1
		elif month == 12:
			months["Dec"] = months["Dec"] + 1
print(str(months))


sum = 0
for item in months:
	sum = sum + months.get(item)
print("All data points: " + str(sum))

first6months = months.get("Jan") + months.get("Feb") + months.get("Mar") + months.get("Apr") + months.get("May") + months.get("Jun")
print("First six months of the year: " + str(first6months))

		
plt.bar(range(len(months)), months.values(), align='center')
plt.xticks(range(len(months)), months.keys())

plt.show()
