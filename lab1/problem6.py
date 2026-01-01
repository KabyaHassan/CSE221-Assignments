N = int(input())
arr = list(map(int, input().split()))
for i in range (N):
    for j in range (N-1-i):
        if (arr[j] % 2== arr[j+1]%2):
            if arr[j] > arr [j+1] :
                arr[j],arr[j+1]=arr[j+1], arr[j]

print (*arr)


