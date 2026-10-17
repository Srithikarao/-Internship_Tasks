# problem 16: Collections.Counter()
# hackerrank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
n = int(input())
shoe_size = Counter(map(int, input().split()))
customers = int(input())
total_money = 0
for _ in range(customers):
  size, price = map(int, input().split())
  if shoe_size[size] > 0:
    total_money += price
    shoe_size[size] -= 1
print(total_money)

