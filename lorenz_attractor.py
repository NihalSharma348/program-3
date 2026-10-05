import time, os
W, H = 70, 30
x, y, z = 0.1, 0.0, 0.0
s, r, b, dt = 10, 28, 8 / 3, 0.005          # classic Lorenz parameters
trail = []
for step in range(4000):
    dx, dy, dz = s * (y - x), x * (r - z) - y, x * y - b * z
    x, y, z = x + dx * dt, y + dy * dt, z + dz * dt   # Euler integration step
    trail = (trail + [(x, z)])[-600:]                  # keep only the recent path
    if step % 5 == 0:
        canvas = [[" "] * W for _ in range(H)]
        for i, (px, pz) in enumerate(trail):
            cx, cy = int(W / 2 + px * 1.4), int(H - 1 - pz * 0.55)
            if 0 <= cx < W and 0 <= cy < H:
                canvas[cy][cx] = ".:*#"[i * 4 // len(trail)]  # older = fainter
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join("".join(row) for row in canvas))
        time.sleep(0.02)
