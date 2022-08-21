n=int(16)
array=[ ]
for i in range(1,n):
    if (i%3==0) and (i%5==0):
        array.append("FizzBuzz")
    if i%3==0 and i%5!=0:
        array.append("Fizz")
    if i%5==0 and i%3!=0:
        array.append("Buzz") 
    if (i%3!=0) and (i%5!=0):
        array.append(str(i))
print(array)