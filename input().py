x, _ = map(int, input().split())
polynomial = input()
if not eval(polynomial.replace('x', str(x))) == 0:
    print(True)
else:
    print(False)
