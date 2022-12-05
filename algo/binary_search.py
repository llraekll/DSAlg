def binary_search(list, target):
    first = 0
    last = len(list) -1
    print("This the last of the list bruh", last)
    print(target, "this bruh?")

    while first <= last:
        midpoint = (first+last)//2
        print("the mid bruh", midpoint)

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            # if the +1 or -1 is not used the program will be on a continous loop as the new number will be the same midpoint
            first = midpoint + 1 
            print("The new first", first)
        else:
            last = midpoint - 1
            print("The new last", last)
    return None


def verify(pos):
    if pos is not None:
        print("bruh found it:", pos)
    else:
        print("I'm sorry bruh")


numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 69]

result = binary_search(numbers, 8)
verify(result)
