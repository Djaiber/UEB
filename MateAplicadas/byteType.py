data = b'\xe5Mx'
binary = ''
for x in data:
    binary += f'{x:0b}'.zfill(8)
print(binary)
print(int(binary, 2))
print(int.from_bytes(data))
a = 15027576
data = a.to_bytes(5)
print(data)
print(len(data))