# string
```
print("hello word")

#hello world
```

# Multiple Items
```
name = "Alice"
age = 25
print("Name:", name, "Age", age)

#Name:ALice Age:25
```

# String Formatting in Print
## Using f-strings
```
name = "Bob"
age = 30
print(f"Name:{name}, Age:{age})

#Name: Bob, Age: 30
```

## Using `%` formatting
```
name = "David"
age  = 40
print("Name:%s, Age:%d" % (name, age))


Name: David, Age: 40
```

## Customizing End Character
By dafault, `print()` adds a newline at the end of the output. You can change this behavior using the `ehd` parameter
```
print("Hello", end = "")
print("World")



Hello World!
```

## Printing with a Separetor
If you're printting multiple items and want a custom separator, you can use the `sep` parameter
```
print("apple", "banana", "cherry", sep = ", ")

#apple, banana, cherry

```