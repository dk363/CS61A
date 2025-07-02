def smallest_prime_factor(n):
    k = 2
    while k <= n:
        if n % k == 0:
            return k
        k += 1
    return n  # 如果 n 是 1 或者没有找到因子，返回 n 本身

def prime_factors(n):
    while n > 1:
        k = smallest_prime_factor(n)
        print(k)
        n = n // k

prime_factors(360)