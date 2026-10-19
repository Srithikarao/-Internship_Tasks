# problem 2 : The Captain's Room
# hackerrank :https://www.hackerrank.com/challenges/py-the-captains-room/problem
n = int(input())
room_list = list(map(int, input().split()))
room_set = set(room_list)
captain_room = (sum(room_set)* n - sum(room_list)) // (n - 1)
print(captain_room)
