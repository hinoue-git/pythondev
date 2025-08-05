
def fibonacci_sequence(n):
    # 1番目の数値は1
    elif n == 1:
        return 1
    # 2番目の数値は1
    elif n == 2:
        return 1
    # 3番目以降の数値は、直前の2つの数値の和
    elif n >= 3:
        return fibonacci_sequence(n - 2) + fibonacci_sequence(n - 1)