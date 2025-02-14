num = int(input("Enter a number: "))
total = sum(int(num[i]) ** (i + 1) for i in range(len(str(num))))
print(f"{num} is a Disarium number." 
if total == num 
else
 f"{num} is NOT a Disarium number.")