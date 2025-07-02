```
for variable in iterable:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
	print(fruit)
```
iterable: The collection of items you want to loop through

# Iterating Through a List
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


apple
banana
cherry

```


# Iterating Through a String 

```
word = "Python"
for char in word:
    print(char)


P
y
t
h
o
n

```


# using range()

```
for i in range(5):
	print(i)

0
1
2
3
4
```

```
for i in range(1, 10, 2): # Start at 1, stop before 10, step by 2
	print(i)

1
3
5
7
9
```

# Iterating Through a Dictionary

```
person = {"name": "Alice", "age": 30, "city": "New York"}

for key in person:
	print(key)

for key, value in person.items():
	print(f"{key}: {value}")

name
age
city

name: Alice
age: 30
city: New York

```


# Iterating Through a Nested Structue

```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
	for num in row:
		print(num, end=" ")
	print()
```


# Using `break` and `continue`

```
for i in range(5):
	if i == 3:
		break
	print(i)

0
1
2
```

```
for i in range(5):
	if i == 3:
		continue
	print(i)

0
1
2
4
```


# Looping With Else

```
for i in range(5):
	print(i)
else:
	print("Loop completed without interruption!")


```