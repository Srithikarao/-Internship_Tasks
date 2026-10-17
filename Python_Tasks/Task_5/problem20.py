# problem 20: Piling Up!
# hackerrank: https://www.hackerrank.com/challenges/piling-up/problem

a = int(input())
for _ in range(a):
    num, cubes = int(input()), list(map(int,input().split()))
    yes_no = "Yes"
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            larger = cubes[0]
            cubes.pop(0)     
        else:
            larger = cubes[-1]
            cubes.pop(-1)  
        if larger < cubes[0] or larger < cubes[-1]:
            yes_no = 'No'
            break
    print(yes_no)
