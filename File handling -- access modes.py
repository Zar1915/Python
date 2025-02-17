file_read = open('Codingal.txt', 'r')
print("File in read mode - ")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode.....")
file_write.write("Writing")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n file in append mode......")
file_append.write("Appending")
file_append.close()