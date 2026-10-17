# problem 13: Nested Lists
# hackerrank: https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique = sorted(list(set([student[1] for student in students])))
    second_lowest = unique[1]
    result = sorted([student[0] for student in students if student[1] == second_lowest])
    for name in result:
        print(name) 

