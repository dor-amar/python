with open('kuku.txt','r') as file:
    content = file.read()
    spaces = content.split()
    count = len(spaces)
    print(count)

