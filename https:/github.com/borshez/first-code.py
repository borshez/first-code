from random import randint

a = []
for i in range(10):
    a.append(randint(1, 50))
    a.sort()
    print(a)
value = int(input())
end = len(a) - 1
start = [0]
mid = (end - start) // 2
cur = a[mid]
if value == cur:
    mid = res
    print(res)
while value > cur:
    start = mid
    mid = (start + end) // 2
    cur = a[mid]
while value < cur:
    end = mid
    mid = (start + end) // 2
    cur = a[mid]
for start in a:
    if start == end:
        break
    print('Такого числа нет в этом массиве!')
