T = int(input())
t_lists = []

for _ in range(T):
    inp = input()
    seg = inp.split()
    name = seg[0]
    destination = seg[-3]
    time = seg[-1]
    t_lists.append([name, destination, time])

for i in range(T):
    for j in range(T - i - 1):
        if t_lists[j][0] > t_lists[j + 1][0]:
            t_lists[j], t_lists[j + 1] = t_lists[j + 1], t_lists[j]
        elif t_lists[j][0] == t_lists[j + 1][0]:
            if t_lists[j][2] < t_lists[j + 1][2]:
                t_lists[j], t_lists[j + 1] = t_lists[j + 1], t_lists[j]

for train in t_lists:
    print(f"{train[0]} will departure for {train[1]} at {train[2]}")
