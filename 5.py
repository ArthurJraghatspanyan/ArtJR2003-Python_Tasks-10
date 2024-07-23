# Use list comprehension to generate a list of squares for all integers from 1 to 10. The resulting list should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

ls = [x ** 2 for x in range(1, 11)]
print(ls)
