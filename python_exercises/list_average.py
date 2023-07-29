from functools import reduce

def average(num_list):
    total = reduce(lambda total, element: total + element, num_list)
    return total/len(num_list)
    
num_list =[1,2,3,4,5,6]
print(average(num_list))
