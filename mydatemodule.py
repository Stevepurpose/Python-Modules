import datetime

#get current date time variable values
print(datetime.datetime.now())
print("year:", datetime.datetime.now().year)
print("month:", datetime.datetime.now().month)
print("weekday", datetime.datetime.now().weekday())


#create date object
myDate = datetime.datetime(2025,1,1,1,1,20)
print(myDate)

#format into string
print(myDate.strftime("%Y, %B, %A"))