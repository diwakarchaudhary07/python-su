# -----------------------------
# Function with arguments
# -----------------------------
def add(a, b):
    return a + b

def greet(name):
    print("Hello,", name)

def convert_to_float(x):
    return float(x)

# Function calls
print("Sum =", add(10, 20))
greet("Rahul")
print("Float Conversion:", convert_to_float(5))

# -----------------------------
# List operations
# -----------------------------
lst = [1, 2, 3]
lst.append(4)
lst.extend([5, 6])
lst.insert(1, 9)
print("\nList after operations:", lst)

# -----------------------------
# Dictionary operations
# -----------------------------
d = {"a": 1, "b": 2}
d.update({"c": 3})
val = d.get("b")
print("\nDictionary:", d, "| Value of b:", val)

# -----------------------------
# Set operations
# -----------------------------
s = {1, 2, 3}
t = {3, 4, 5}
print("\nUnion:", s.union(t))
print("Intersection:", s.intersection(t))
print("Difference:", s.difference(t))

# -----------------------------
# Tuple operations
# -----------------------------
tup = (1, 2, 3, 2, 4)
print("\nTuple:", tup)
print("Count of 2:", tup.count(2))
print("Index of 4:", tup.index(4))

# -----------------------------
# Type Casting
# -----------------------------
num = 100
snum = str(num)
fnum = float(num)
lst_from_tuple = list(tup)
set_from_list = set(lst)
print("\nType Casting Examples:")
print(snum, type(snum))
print(fnum, type(fnum))
print(lst_from_tuple, type(lst_from_tuple))
print(set_from_list, type(set_from_list))
