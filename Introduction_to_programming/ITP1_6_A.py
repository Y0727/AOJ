n = int(input())
num_list = list(map(int, input().split()))
num_list.reverse()

for i in range(n):
    print(num_list[i], end="")
    if i < n-1:
        print(" ", end="")

print()