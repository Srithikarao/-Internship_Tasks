
# problem 12: Introduction to Sets
#hackerrank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    w = set(array)
    return sum(w)/len(w)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
