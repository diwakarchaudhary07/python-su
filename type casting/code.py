# int to float
x = 10
y = float(x)
print(y, type(y))   # 10.0 <class 'float'>

# float to int
a = 9.8
b = int(a)
print(b, type(b))   # 9 <class 'int'>

# int to string
num = 123
s = str(num)
print(s, type(s))   # "123" <class 'str'>

# string to int
st = "456"
n = int(st)
print(n, type(n))   # 456 <class 'int'>

# list to tuple
lst = [1,2,3]
t = tuple(lst)
print(t, type(t))   # (1,2,3) <class 'tuple'>

# tuple to set
tp = (1,2,2,3)
s = set(tp)
print(s, type(s))   # {1,2,3} <class 'set'}

# list of pairs to dict
pairs = [("a",1),("b",2)]
d = dict(pairs)
print(d, type(d))   # {'a':1,'b':2} <class 'dict'>
