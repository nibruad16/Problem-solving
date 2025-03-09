# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

t = int(input())

for _ in range(t):
    string = input()
    if string[-1] == "u":
        print("JAPANESE")
    elif string[-1] == "o":
        print("FILIPINO")
    else:
        print("KOREAN")