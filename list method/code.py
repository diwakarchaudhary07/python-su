# Starting list
lst = [3, 1, 4, 1, 5]

print("Original List:", lst)

# 1. append()
lst.append(9)
print("After append:", lst)

# 2. extend()
lst.extend([2, 6])
print("After extend:", lst)

# 3. insert()
lst.insert(2, 7)
print("After insert:", lst)

# 4. remove()
lst.remove(1)   # removes first 1
print("After remove:", lst)

# 5. pop()
popped = lst.pop()   # removes last element
print("After pop:", lst, "| Popped:", popped)

# 6. clear()
temp = lst.copy()    # save copy before clearing
lst.clear()
print("After clear:", lst)

# Restore list for next methods
lst = temp.copy()

# 7. index()
idx = lst.index(7)
print("Index of 7:", idx)

# 8. count()
cnt = lst.count(1)
print("Count of 1:", cnt)

# 9. sort()
lst.sort()
print("After sort:", lst)

# 10. reverse()
lst.reverse()
print("After reverse:", lst)

# 11. copy()
new_lst = lst.copy()
print("Copied List:", new_lst)
