```
def if_ (c, t, f):
	if c:
		return t
	else:
		return f

from math import sqrt

def real_sqrt(x):
	return if_(x > 0, sqrt(x), 0.0)


# before we call if_, we will evaluate the () first, it means when we input some negtative numbers, the if_ will not work
```

**function always evaluate their components, but contral statements skip some parts or repeat some parts**