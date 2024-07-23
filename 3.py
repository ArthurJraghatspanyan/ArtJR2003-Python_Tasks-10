#Write a program that removes and returns the last element of a list without using the pop() method.
#If the list is empty, return a message indicating it is empty. Example usage on [1, 2, 3] should return 3 and the list becomes [1, 2]

ls = [1, 2, 3]
print(f"Our original list: {ls}")
element = len(ls)
if not ls:
	print("List is empty: ")
else:
	for i in range(element):
		if ls[i] == element:
			ls = ls[:element - 1]
			break
	print(f"Removed element is: {element}")
	print(f"Our updated list is: {ls}")
