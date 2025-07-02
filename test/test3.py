def sum_digits(n):
    """返回正整数 n 的所有数字位之和"""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last
    
