# https://www.acmicpc.net/problem/1264
while True:
    data = input().lower()
    if data == '#':
        break
    count = 0
    for c in data:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    print(count)
