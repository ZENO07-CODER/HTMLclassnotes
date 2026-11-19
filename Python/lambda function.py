#Map()
numbers = input("Enter ',' seperated number").split(sep=',')
l = list(map(int,numbers))
t = tuple(map(lambda n:n**0.5, l))
print (numbers)

l = []
for num in numbers:
    l.append(int (num)**0.5)

print(l)

#Lambda function
power = lambda x, y: x ** y
print(power(2,3))
