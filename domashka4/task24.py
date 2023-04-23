n = int(input()) 
a = list(map(int, input().split()))  

max_berry_count = 0  
for i in range(n):
    berry_count = a[i]
    if i < n - 1:
        berry_count = max(berry_count, a[i] + a[i+1])
    if i > 0:
        berry_count = max(berry_count, a[i] + a[i-1])
    max_berry_count = max(max_berry_count, berry_count)

print(max_berry_count)
