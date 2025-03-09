# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

n = int(input())
events = defaultdict(int)

for _ in range(n):
    birth, death = map(int, input().split())
    events[birth] += 1
    events[death] -= 1  

years = sorted(events.keys())

max_people = 0
year = 0
current_population = 0

for y in years:
    current_population += events[y]
    if current_population > max_people:
        max_people = current_population
        year = y 

print(year, max_people)