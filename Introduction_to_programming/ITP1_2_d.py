W, H, x, y, r = map(int, input().split())

W_left = x
W_right = W - x
H_bottom = y
H_top = H - y

if r <= W_left and r <= W_right and r <= H_bottom and r <= H_top:
    print("Yes")
else:
    print("No")