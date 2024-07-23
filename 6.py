#Write a single line of Python using list comprehension to filter and create a list of even numbers from an existing list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], resulting in [2, 4, 6, 8, 10].

print([x for x in range(1, 11) if x % 2 == 0])
