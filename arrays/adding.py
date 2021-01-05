import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 34   
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])   
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

numbers.append(6)
numbers.insert(5,0)

numbers2 = arr.array('i', [10,20,20])
numbers.extend(numbers2)
print(numbers) 