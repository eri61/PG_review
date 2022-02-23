# %% 6-A
input_data = input()
print(" ".join(input().split()[::-1]))

# %% 6-B
trial = int(input())
num = set(range(1, 14))
dict_input = {"S": [], "H": [], "C": [], "D": []}

# input関数を使って入力をディクショナリで管理
for i in range(trial):
    r, n = input().split(" ")
    dict_input[r].append(int(n))

# 出力
for key, val in dict_input.items():
    out = num - set(val)
    for i in sorted(out):
        print(f"{key} {i}")

# %% 6-C
room = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())

for i in range(n):
    b, f, r, v = map(int, input().split())
    room[b-1][f-1][r-1] += v

for i in range(len(room)):
    for j in range(len(room[i])):
        print('', *room[i][j])
    if i != len(room[i]):
        print('#'*20)
