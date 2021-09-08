from random import randint

a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)
value = int(input())
end = len(a) - 1
start = 0
mid = (end - start) // 2
cur = a[mid]
while value != cur and end - start > 1:
    if value > cur:
        start = mid
    else:
        end = mid
    mid = (start + end) // 2
    cur = a[mid]
if end - start <= 1:
    print('Число не найдено')
else:
    print(mid)
    