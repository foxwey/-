def dayUP(df):
    dayup = 1.0
    for i in range(365):
	    if i % 7 in [6,0]:
		    dayup = dayup*(1-df)
	    else:
		    dayup = dayup*(1+df)
    return dayup


dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
	dayfactor +=0.001

print("工作日多努力的力量{:.2f}才能超过每天努力1%".format(dayfactor))