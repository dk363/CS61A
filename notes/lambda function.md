```
square = lambda x: x * x

square(10)
100


add_one = lambda x: x + 1

add_one(9)
10
```

no return

single exepression

if your goal is to pass a function that's just does something simpl, use lambda

# Lamda Exepression Versus Def Statements

# only the def gives the function an intrinstic name
```
square = lambda x: x * x

square
function <lambda> at ...
```


```
def square(x):
	return x * x

square
function square at ... 
```

```
lambda x: x + 1

if we do not give a name to the lambda expression, we will lost it 
```