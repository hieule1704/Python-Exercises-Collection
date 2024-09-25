# Cho các biến với giá trị:
i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

# Tạo một dictionary để lưu kết quả
results = {}

# (a) i1 + (i2 * i3)
results['a'] = i1 + (i2 * i3)

# (b) i1 * (i2 + i3)
results['b'] = i1 * (i2 + i3)

# (c) i1 / (i2 + i3)
results['c'] = i1 / (i2 + i3)

# (d) i1 // (i2 + i3)
results['d'] = i1 // (i2 + i3)

# (e) i1 / i2 + i3
results['e'] = i1 / i2 + i3

# (f) i1 // i2 + i3
results['f'] = i1 // i2 + i3

# (g) 3 + 4 + 5 / 3
results['g'] = 3 + 4 + 5 / 3

# (h) 3 + 4 + 5 // 3
results['h'] = 3 + 4 + 5 // 3

# (i) (3 + 4 + 5) / 3
results['i'] = (3 + 4 + 5) / 3

# (j) (3 + 4 + 5) // 3
results['j'] = (3 + 4 + 5) // 3

# (k) d1 + (d2 * d3)
results['k'] = d1 + (d2 * d3)

# (l) d1 + d2 * d3
results['l'] = d1 + d2 * d3

# (m) d1 / d2 - d3
results['m'] = d1 / d2 - d3

# (n) d1 / (d2 - d3)
results['n'] = d1 / (d2 - d3)

# (o) d1 + d2 + d3 / 3
results['o'] = d1 + d2 + d3 / 3

# (p) (d1 + d2 + d3) / 3
results['p'] = (d1 + d2 + d3) / 3

# (q) d1 + d2 + (d3 / 3)
results['q'] = d1 + d2 + (d3 / 3)

# (r) 3 * (d1 + d2) * (d1 - d3)
results['r'] = 3 * (d1 + d2) * (d1 - d3)

# In kết quả
for key, value in results.items():
    print(f"Kết quả của lệnh {key}: {value}")