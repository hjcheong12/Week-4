l, x = map(int, input().split())
number = list(map(int, input().split()))

result = []

for i in number:
    if i > x:
        result.append(i)


print(result)