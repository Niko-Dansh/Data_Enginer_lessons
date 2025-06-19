import math

# --- параметры ---
N = 200   # число точек
# коэффициент, подгоняющий высоту к ≈1 м
scale_y = 0.727 / 16
# смещение по Y, чтобы центрирование было по середине высоты
offset_y = 0.272

xs = []
ys = []

for i in range(N):
    t = 2 * math.pi * i / N
    x = 0.5 * math.sin(t)**3
    # классическая «сердечная» формула в скейле
    raw_y = (13*math.cos(t)
             - 5*math.cos(2*t)
             - 2*math.cos(3*t)
             -   math.cos(4*t))
    y = scale_y * raw_y + offset_y

    xs.append(round(x, 6))
    ys.append(round(y, 6))

# --- выводим массивы в консоль ---
print("X =", xs)
print("Y =", ys)

# --- готовим .scr для AutoCAD ---
with open("heart.scr", "w") as f:
    f.write("._PLINE\n")
    for x, y in zip(xs, ys):
        f.write(f"{x},{y}\n")
    f.write("C\n")   # Close polyline