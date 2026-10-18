# problem 16 : Check Subset
# hackerrank: https://www.hackerrank.com/challenges/py-check-subset/problem


a = int(input())
for _ in range(a):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    if A.issubset(B):
        print(True)
    else:
        print(False)
