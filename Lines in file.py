file = open('Codingal.txt', 'r')
counter = 0
Content = file.read()
Colist = Content.split("\n")
for i in Colist:
    if i:
            counter += 1
print("This is the number of lines in the file ")
print(counter)
