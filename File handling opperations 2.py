file_read = open('Codingal.txt', 'r')
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode.....")
file_write.write("Hi I am a Penguin and i amd 1 year old")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n file in append mode")
file_append.write("I am a Penguin and i am 1 year old")
file_append.close()