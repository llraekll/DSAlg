def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            print(list[midpoint])
            return True
        else:
            if list[midpoint] < target:
                print('if', list)
                return recursive_binary(list[midpoint+1:], target)

            else:
                print('else', list)
                return recursive_binary(list[:midpoint], target)


def verify(result):
    print("Meow meow nigga:", result)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 69]
result = recursive_binary(numbers, 5)
verify(result)
