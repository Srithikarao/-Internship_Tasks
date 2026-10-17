# problem 8: Set .add()
# hackerrank: https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())
c = set()
for _ in range(n):
    c.add(input())
print(len(c))
