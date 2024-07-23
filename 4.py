# Develop a program that clears all elements from a list without using the clear() method. After running the function on [1, 2, 3], the list should be empty.

ls = [1, 2, 3]
print(f"Our original list: {ls}")
for i in range(len(ls)):
	ls = ls[i:]

print(f"Our updated list: {ls}")
