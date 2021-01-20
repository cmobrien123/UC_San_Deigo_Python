#Pattern:
#starting number = 10,0000
#subtract 100 to get the output, then 99, then 98 and so on
#continue this number the "subtraction number" is less than 10
#at that point, the subtraction number becomes 100 again
#continue this until the output is 0
x=10000
y=100
print(x)
while x > 0 and y>9:
    x=x-y
    y=y-1
    print(x)
    if y is 9: y=100
