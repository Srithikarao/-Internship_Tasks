# problem 17: No Idea!
# hackerrank: https://www.hackerrank.com/challenges/no-idea/problem
def cal_happiness(arr, A, B):
    happiness = 0
    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)
if __name__ == '__main__':
    n, k = input().split()
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    cal_happiness(arr, A, B)

