new_file = open('New_file.txt', 'x')
new_file.close()
import os
print("Checking if my_file exists or not")
if os.path.exists("my_file1.txt"):
    os.remove('my_file1.txt')
else:
    print("The file does not exist")
my_file = open('my_file.txt', 'w')
my_file.write("I am Penguin and i am 1yr old")
my_file.close()
os.remove('Codingal.txt')
os.rmdir('Folder')