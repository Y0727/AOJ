while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break

    for w in range(W):
        for h in range(H):
            if h == 0 or h == H-1 or w == 0 or w == W-1:
                print("#", end="")
            else:
                print(".", end="")
        print()

    print()