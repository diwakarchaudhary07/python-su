# -----------------------------
# 1. List Methods
# -----------------------------
lst = [3, 1, 4, 1, 5]
print("Original List:", lst)

lst.append(9)
lst.extend([2, 6])
lst.insert(2, 7)
lst.remove(1)
popped = lst.pop()
lst.sort()
lst.reverse()
new_lst = lst.copy()
print("Final List:", new_lst)

# -----------------------------
# 2. Dictionary Methods
# -----------------------------
d = {"a": 1, "b": 2, "c": 3}
print("\nOriginal Dict:", d)

val = d.get("a")
d.update({"b": 20})
pair = d.popitem()
d.setdefault("z", 99)
new_d = d.copy()
print("Final Dict:", new_d)

# -----------------------------
# 3. Set Methods
# -----------------------------
s = {1, 2, 3}
t = {3, 4, 5}
print("\nOriginal Set:", s)

s.add(6)
s.update([7, 8])
s.discard(10)
union_set = s.union(t)
inter_set = s.intersection(t)
diff_set = s.difference(t)
sym_diff = s.symmetric_difference(t)
print("Union:", union_set)
print("Intersection:", inter_set)
print("Difference:", diff_set)
print("Symmetric Difference:", sym_diff)

# -----------------------------
# 4. Tuple Methods
# -----------------------------
tup = (1, 2, 3, 2, 4, 5, 2)
print("\nTuple:", tup)
print("Count of 2:", tup.count(2))
print("Index of 4:", tup.index(4))

# -----------------------------
# 5. Type Casting
# -----------------------------
num = 123
snum = str(num)
fnum = float(num)
lst_from_tuple = list(tup)
set_from_list = set(lst)
dict_from_pairs = dict([("x", 10), ("y", 20)])
print("\nType Casting Examples:")
print(snum, type(snum))
print(fnum, type(fnum))
print(lst_from_tuple, type(lst_from_tuple))
print(set_from_list, type(set_from_list))
print(dict_from_pairs, type(dict_from_pairs))

# -----------------------------
# 6. Function Without Argument
# -----------------------------
def greet():
    print("\nHello, Welcome to Python Functions!")

def show_sum():
    a, b = 5, 10
    print("Sum =", a + b)

# Function calls
greet()
show_sum()
# function without argument