numBooks = int(input('Enter the number of books you purchased this month:\n'))
if numBooks <=1:
    points = 0
elif numBooks <=3:
    points = 5
elif numBooks <=-5:
    points = 15
elif numBooks <=7:
    points = 30
else:
    points =60

print('You have earned {} points this month.'.format(points))