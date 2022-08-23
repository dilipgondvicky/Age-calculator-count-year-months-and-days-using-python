#dilipgondvicky
import datetime
def ageCalculate(year, month, date):
    today = datetime.datetime.now().date()
    dob = datetime.date(year, month, date)
    years= ((today-dob).total_seconds()/ (365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    print('You Are {0} Years, {1} Months And {2} Days Old. \n'.format(yearsInt,monthsInt,daysInt))
while True:
    yearinp = int(input("Enter Year Of Birth :\t"))
    monthsinp = int(input("Enter Month of Birth:\t"))
    dateinp = int(input("Enter Date :\t"))
    ageCalculate(yearinp, monthsinp, dateinp)
    a = input('Type yes to Continue \n Type Somenthing To Exit \n') 
    if a == 'yes':
        continue
    else:
        break
