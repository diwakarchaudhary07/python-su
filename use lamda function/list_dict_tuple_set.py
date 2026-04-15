def process_data(lst, d, t, s):

    # List → square
    list_result = list(map(lambda x: x**2, lst))

    # Dictionary → double values
    dict_result = dict(map(lambda item: (item[0], item[1]*2), d.items()))

    # Tuple → add 10
    tuple_result = tuple(map(lambda x: x + 10, t))

    # Set → cube
    set_result = set(map(lambda x: x**3, s))

    return list_result, dict_result, tuple_result, set_result


# Input data
lst = [1, 2, 3]
d = {"a": 1, "b": 2}
t = (4, 5, 6)
s = {2, 3, 4}

# Function call
result = process_data(lst, d, t, s)

# Output
print("List:", result[0])
print("Dict:", result[1])
print("Tuple:", result[2])
print("Set:", result[3])