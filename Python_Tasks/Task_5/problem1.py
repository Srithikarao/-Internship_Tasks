# porblem1: Find the Runner-Up Score!
# hackerrank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a = sorted(list(set(arr)))
    print(a[-2])      
