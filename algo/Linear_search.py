def linear_search(list, target):
# this shows that there is a range of numbers from 0 to mentioned in the list
    for i in range(0, len(list)): 
        print(i)
        if list[i] == target:
            print(i)
            return i
    return None

def verify(target):
    if target is not None:
        print('Target found at index:', target)
    else:
        print('Target not found')
    
numbers = [2,3,4,5,6,7,8,9,10,1,9832478934]

result = linear_search(numbers,9832478934)
verify(result)

result = linear_search(numbers,7)
verify(result)