def my__generator():
    yield 1
    yield 2
    yield 3

for value in my__generator():
    print(value)    