import math

repeat = int(input())

for _ in range(repeat) :
    A, B = map(int, input().split())
    print(int((A*B)/math.gcd(A,B)))