T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))


    is_ascending = True
    for i in range (N):
        for j in range (N-1-i):
            if arr[j] > arr [j+1]:
                is_ascending = False

    if is_ascending == True:
        print("YES")
    else:
        print("NO")
                


