# Write a program that removes the first occurrence of a specified element from a list without using the remove() method. If the element does not exist, print a message. Example: Remove 2 from [1, 2, 3, 2, 4] resulting in [1, 3, 2, 4]

ls = [1, 2, 3, 4, 5]
element = 2

print(f"Our original ls is: {ls}")

print(f"Our element to remove is: {element}")

if element in ls:
	for i in range(len(ls)):
		if ls[i] == element:
			ls = ls[:i] + ls[i+1:]
			break
	print(f"Out updated ls is: {ls}")
else:
	print("Element not found")
