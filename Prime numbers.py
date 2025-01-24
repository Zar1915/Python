num = 20
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print("This is not a prime number")
else:
    print("This is a prime number")    
