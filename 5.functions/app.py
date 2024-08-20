def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False            
        i += 1
    return True
            
        

def common_nums(list1,list2):
    new_list = []
    for x in list1:
        if x in list2:
            new_list.append(x)
    return new_list


list1 = [1,2,3,4,5]
list2 = [1,7,3,9,20]
print(common_nums(list1,list2))







