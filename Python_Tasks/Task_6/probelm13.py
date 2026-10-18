# problem 13: Set .union() Operation
# hackerrank: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
eng = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
result = eng.union(french)
print(len(result))
