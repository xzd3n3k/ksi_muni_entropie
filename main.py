import math

p_first = [0.0927, 0.0592, 0.0158, 0.0592, 0.0473, 0.0316, 0.0316, 0.0296, 0.0434, 0.0513, 0.0493, 0.075, 0.0848, 0.0256, 0.0178, 0.0178, 0.0, 0.075, 0.069, 0.0178, 0.0039, 0.0671, 0.0, 0.002, 0.0, 0.0335]

entropy_A = -sum(p * math.log2(p) if p != 0 else 0 for p in p_first)

print(f"Entropie náhodné veličiny A: {entropy_A}")
p_last = [0.86, 0.0, 0.0, 0.0039, 0.1045, 0.0, 0.0, 0.0, 0.002, 0.0, 0.0, 0.0039, 0.002, 0.0118, 0.0, 0.0, 0.0, 0.0039, 0.0039, 0.0039, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

entropy_B = -sum(p * math.log2(p) if p != 0 else 0 for p in p_last)

print(f"Entropie náhodné veličiny B: {entropy_B}")
