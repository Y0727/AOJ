while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for w in range(W):
        for h in range(H):
            print("#", end="")
        print()

    print()