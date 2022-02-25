# %%
for i in range(1000):
    print("Hello world")

# %%
val = list(iter(input, '0'))
ren = len(val)
for i, v in enumerate(val):
    print(f'Case {i+1}: {v}')

# %%
a, b = map(int, input().split())
while a or b:
    print(a, b)
    a, b = sorted(map(int, input().split()))

# another solusion
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    else:
        sorted([x, y])
        print(x, y)

# %%
count = 0
a, b, c = map(int, input().split())

for i in range(a, b+1):
    count += (c % i == 0)

print(count)
