
# problem 20: No Idea!
# hackerrank: https://www.hackerrank.com/challenges/no-idea/problem

def cal_happiness(arr, A, B):
    h = 0
    for i in arr:
        if i in A:
            h += 1
        elif i in B:
            h -= 1
    print(h)

if __name__ == '__main__':
    n, k = input().split()
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    cal_happiness(arr, A, B)
