NumberOfYears = int(input('Enter the number of years for which you have rainfall data.\n'))

ListOfMonths = ['January','February','March','April','May','June','July','August','September','October','November','December']

monthsCount=1
rainSum=0

for year in range(NumberOfYears ):
    for month in ListOfMonths:
        rainSum+= int(input('Enter the rainfall in inches from year {} in the month of {}\n'.format(year+1, month)))
        monthsCount +=1

AverageRain = rainSum/monthsCount

print('The number of months is:',monthsCount )
print('The total inches of rain is:',rainSum)
print('The average inches of rain per month is:',AverageRain)