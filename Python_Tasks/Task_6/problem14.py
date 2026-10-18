# problem 14:Set .intersection() Operation
# hackerrank: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n = int(input())
eng = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
result = eng.intersection(french)
print(len(result))

