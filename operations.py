from functools import reduce

operations_dict = {
    "1": lambda *args: sum(args),
    "2": lambda *args: reduce(lambda x, y: x * y, args),
    "3": lambda *args: sum(map(lambda x: x * x, args))
}

print(operations_dict["3"](1, 5, 5, 3, 2))
