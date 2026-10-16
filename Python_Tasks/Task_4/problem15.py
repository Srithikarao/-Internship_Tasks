# problem 15 : Word Order
# hackerrank: https://www.hackerrank.com/challenges/word-order/problem

n=int(input())
d ={}
for i in range(n):
    word = input()
    if word in d:
        d[word]+=1
    else:
        d[word]=1
print(len(d))
print(*d.values())
