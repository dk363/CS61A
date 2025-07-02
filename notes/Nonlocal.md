It allows you to modift a variable from an outer (encloseing) function inside a nested function
```
def outter_function():
	x = 10
	print(x)
	def inner_function():
		x = 20
		print(x)


10
20



def outter_function():
	x = 10
	print(x)
	def inner_function():
		nonlocal x
		x = 20
		print(x)


20
20
```

