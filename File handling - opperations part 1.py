file = open('Codingal.txt', 'r')
print("File in read mode - ")
print(file.read())
file.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode")
file_write.write("Codingal has a pet called Penguin.")
file_write.close()

file_append = open('Codingal.txt', 'a')
print("file in append mode")
file_append.write("Penguin likes codingal because codingal feeds it. Codingal likes having a pet")
file_append.close()