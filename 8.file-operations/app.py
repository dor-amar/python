file = open('example.txt','r')

print(file.read()) 
print(file.read(20))

print(file.readline())
print(file.readline())
print(file.readline())

for line in file: 
    print(line)

file.close()

file2 = open("file2.txt",'a')
file2.writelines("Last Line \n")
file2.writelines("Last Line \n")
file2.write("Last Line")
file2.close()

f = open("file2.txt",'w')
f.write("Override")
f.close()

f = open("new__file.txt", 'w')
f.write("Hello")
f.close()

f = open("dor_file.tf",'x')

import os 
if not os.path.exists("dor_file.txt"):
    f = open("dor_file.txt",'x')
    f.close()
