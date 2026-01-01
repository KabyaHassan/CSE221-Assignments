T = int(input())

for _ in range(T):
    N = int(input())
    arr_id = list(map(int, input().split()))
    arr_mark = list(map(int, input().split()))

    count = 0
    for i in range(N - 1):
        best_index = i
        for j in range(i + 1, N):
            if arr_mark[j] > arr_mark[best_index]:
                best_index = j
            elif arr_mark[j] == arr_mark[best_index] and arr_id[j] < arr_id[best_index]:
                best_index = j
        if i != best_index:
            arr_mark[i], arr_mark[best_index] = arr_mark[best_index], arr_mark[i]
            arr_id[i], arr_id[best_index] = arr_id[best_index], arr_id[i]
            count += 1

    print(f"Minimum swaps: {count}")
    for i in range(N):
        print(f"ID: {arr_id[i]} Mark: {arr_mark[i]}")
         
