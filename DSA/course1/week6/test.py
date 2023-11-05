ops_map = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '*': lambda x, y: x * y,
               '/': lambda x, y: x / y}

x = 1
y = 2
print(ops_map['+'](x, y))