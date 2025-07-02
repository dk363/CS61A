"""Generalization"""

def make_adder(n):
    def adder(k):
        return k + n 
    return adder
"""
add_three = make_adder(3)

add_three(5)

8
"""