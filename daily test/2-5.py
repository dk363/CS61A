class Accumlator:
    def __init__(self):
        self.total = 0
    
    def __call__(self, value):
        self.total += value
        return self.total

acc = Accumlator()

print(acc(5))
print(acc(19))