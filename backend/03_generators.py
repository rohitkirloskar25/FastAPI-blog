def return_values():
    yield 1
    yield 2
    yield "three"

value = return_values()
print(value.__next__())  # Output: 1
print(value.__next__())  # Output: 2
print(value.__next__())  # Output: "three"