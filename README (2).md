# Lorenz Attractor Terminal Animation

A 19-line Python program that simulates the Lorenz system and animates its famous "butterfly" trajectory right in your terminal. No external libraries required.

## About

The Lorenz system is a set of three coupled differential equations, introduced by Edward Lorenz in 1963 to model atmospheric convection. It is a classic example of **chaos**: the system is fully deterministic, yet its long-term behavior never repeats and is extremely sensitive to the starting conditions.

The equations used:

```
dx/dt = σ (y − x)
dy/dt = x (ρ − z) − y
dz/dt = x y − β z
```

with the classic parameters σ = 10, ρ = 28, β = 8/3.

## Prerequisites

- Python 3.x
- A terminal at least 70 columns wide and 30 rows tall
- No pip packages needed (uses only the built-in `time` and `os` modules)

## How to Run

```bash
python lorenz_attractor.py
```

## How It Works

1. Start at the point (0.1, 0, 0) with a time step `dt = 0.005`.
2. Compute the rate of change of x, y, z from the equations above.
3. Update the position using Euler's method.
4. Keep the latest 600 (x, z) points as a trail.
5. Every 5 steps, draw the trail on a 70×30 text canvas. Newer points are drawn as `#` and older points fade through `*` and `:` to `.`.
6. Clear the screen, print the frame, and repeat for 4000 steps.

## Expected Output

A glowing trail traces the butterfly shape in the x–z plane. The path loops around one lobe, then switches to the other at seemingly random moments, and never settles into a repeating cycle.

## Customization

| Variable | Default | Effect |
|----------|---------|--------|
| `W`, `H` | 70, 30 | Canvas width and height |
| `r` | 28 | Chaos level. Below about 24.7 the trail settles into a fixed point instead of staying chaotic |
| `dt` | 0.005 | Time step. Smaller is more accurate but slower |
| `[-600:]` | 600 | Trail length |
| `range(4000)` | 4000 | Total number of simulation steps |
| `time.sleep` | 0.02 | Delay between frames (animation speed) |

## Limitations

- Euler integration is only first-order accurate. A higher-order method such as Runge–Kutta (RK4) would give more precise trajectories.
- The animation shows only the x–z projection of the 3D attractor.

## License

Free to use and modify for learning purposes.
