# file = open('example.txt','r')

# print(file.read()) 
# print(file.read(20))

# print(file.readline())
# print(file.readline())
# print(file.readline())

# for line in file: 
#     print(line)

# file.close()

# file2 = open("file2.txt",'a')
# file2.writelines("Last Line \n")
# file2.writelines("Last Line \n")
# file2.write("Last Line")
# file2.close()

# f = open("file2.txt",'w')
# f.write("Override")
# f.close()

# f = open("new__file.txt", 'w')
# f.write("Hello")
# f.close()

# f = open("dor_file.tf",'x')

# import os 
# if not os.path.exists("dor_file.txt"):
#     f = open("dor_file.txt",'x')
#     f.close()

# if os.path.exists("dor_file.tf"):
#     os.remove("dor_file.tf")
# else: 
#     print("File not exits")


# with open('example.txt','r') as file:
#     content = file.read()
#     print(content)


# Open a file and write to it 
with open("my_file.txt",'w') as file: 
    file.write("Hello, My File ! ")

# Append to the file 
with open("my_file.txt",'a') as file: 
    file.write(" \n Hello, My File ! ")