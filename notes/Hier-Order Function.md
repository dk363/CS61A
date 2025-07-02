# return function
```
def make_adder(n):

    def adder(k):

        return k + n

    return adder


"""
add_5 = make_adder(5)
	make_adder(5):
		def adder(k):
			return k + 5
		return adder

result = adder(10)
print(result)
15


make_adder(1)(2)
3

make_addder(2000)(24)
2024
"""
```

 