# problem 10: Designer Door Mat
# hackerrank: https://www.hackerrank.com/challenges/designer-door-mat/problem
n,k = map(int, input().split())
for i in range(1, n, 2):
    print((".|." * i).center(k, "-"))
print("WELCOME".center(k,"-"))
for i in range(n - 2, 0, -2):
    print((".|." * i).center(k, "-"))

