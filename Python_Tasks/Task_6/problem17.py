# problem 17 : Check Strict Superset
# hackerrank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem
A = set(map(int, input().split()))
n = int(input())
result = True
for _ in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B) or A == B:
        result = False
        break
print(result)

