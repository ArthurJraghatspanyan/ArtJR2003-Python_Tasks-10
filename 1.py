# Write a program that inserts a value at a specified index in a list without using the built-in insert() method. For example, insert the value 3 at index 1 in the list [1, 2, 4, 5] to make it [1, 3, 2, 4, 5]

ls = [1, 2, 4, 5]
num = [3]
position = 1
ls[position:position] = num
print(ls)
