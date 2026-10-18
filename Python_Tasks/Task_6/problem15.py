# problem 15 : Set .difference() Operation
# hackerrank: https://www.hackerrank.com/challenges/py-set-difference-operation/problem


n = int(input())
eng = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
result = eng.difference(french)
print(len(result))
