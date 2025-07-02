# AKA 时间复杂度/空间复杂度

# MEMOIZATION
```
def memo(f):
	cache = {}
	def memoizzed(n):
		if n not in cache:
			cache[n] = f[n]
		return chche[n]
	return memoized
```
