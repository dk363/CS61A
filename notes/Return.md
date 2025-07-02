```
 def search(f):

    x = 0

    while True:

        if f(x):

            return x

        x += 1

  
  

def square(x):

    return x * x

  

def positive(x):

    return max(0, square(x) - 100)

# 0 is False

if 判定为真时，进入if语句，return x(有点像break)
```



