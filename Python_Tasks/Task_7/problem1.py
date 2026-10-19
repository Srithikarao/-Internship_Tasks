# problem 1 : Set .symmetric_difference() Operation
# hackerrank : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
eng = set(map(int, input().split()))
b = int(input())
french = set(map(int, input().split()))
result = eng.symmetric_difference(french)
print(len(result))
