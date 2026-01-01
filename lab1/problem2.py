T= int (input())

for i in range(T):
    inp = input()
    slices = inp.split()
    d1 = int(slices[1])
    exp = slices[2]
    d2 = float(slices[3])

    if exp == "+":
        ans = d1 + d2
    elif exp == "-":
        ans = d1 - d2
    elif exp == "*":
        ans = d1*d2
    elif exp == "/":
        ans = d1/d2 

    print(ans)
