# problem 12 : Set .discard(), .remove() & .pop()
# hackerrank: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


n = int(input())
s = set(map(int, input().split()))
a = int(input())
for _ in range(a):
    command = input().split()
    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))
