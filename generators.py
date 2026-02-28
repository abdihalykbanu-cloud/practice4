# generators.py
# Python Iterators and Generators Exercises (alternative examples)

print("1. Iterate through a tuple using iter() and next():")
fruits = ("apple", "banana", "cherry")
it = iter(fruits)
print(next(it))  # apple
print(next(it))  # banana
print(next(it))  # cherry

print("\n2. Loop through an iterator of a string:")
word = "Python"
for char in iter(word):
    print(char)

print("\n3. Custom iterator that returns even numbers up to a limit:")

class EvenNumbers:
    def __init__(self, limit):
        self.num = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.limit:
            return self.num
        else:
            raise StopIteration

evens = EvenNumbers(10)
for e in evens:
    print(e)

print("\n4. Generator function that yields squares of numbers:")

def square_gen(n):
    for i in range(1, n+1):
        yield i*i

for val in square_gen(5):
    print(val)

print("\n5. Generator expression to get cubes of numbers:")
cubes = (x**3 for x in range(1, 6))
for c in cubes:
    print(c)