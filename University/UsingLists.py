#Compute a grade in the module based on a list of marks

#Input
marks = [50, 60, 10, 0]

#Find the lowest of the marks
lowest = marks[0]
for mark in marks:
    if mark < lowest:
        lowest = mark

#Compute the mean of the best 3 marks

total = 0

for mark in marks:
    total += mark

total -= lowest
mean = total / 3

#Compute the grade for the given mean

if mean < 30:
    grade = 'fail'
elif mean < 40:
    grade = 'resit'
else:
    grade = 'pass'

print('The grade is:', grade)
print('mean is:', mean)
