# problem 7:Symmetric Difference
# hackerrank: https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
a = set(map(int, input().split()))    
n = int(input())
b = set(map(int, input().split()))
sd = a.symmetric_difference(b)
for i in sorted(sd):
    print(i)
    
