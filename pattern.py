import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Equation: Z(t) = exp(i*t) + exp(i*3.14*t)

# Generate values of t
t = np.linspace(0, 100 * np.pi, 12000)

# Calculate real and imaginary parts
x = np.cos(t) + np.cos(3.14 * t)
y = np.sin(t) + np.sin(3.14 * t)

# Set up the figure
fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect("equal")
ax.axis("off")

# Curve and moving point
(line,) = ax.plot([], [], color="white", linewidth=0.45)
(point,) = ax.plot([], [], "o", color="#00ffff", markersize=4)

# Display the current angle
label = ax.text(
    0.5, 0.96, "", transform=ax.transAxes, color="#00ffff", ha="center", fontsize=12
)


def update(frame):
    # Progressively draw the curve
    end = max(2, int((frame + 1) * len(t) / 240))

    line.set_data(x[:end], y[:end])
    point.set_data([x[end - 1]], [y[end - 1]])

    label.set_text(f"t = {t[end - 1]:.2f} radians")

    return line, point, label


animation = FuncAnimation(fig, update, frames=240, interval=30, blit=True)

# Save as an animated GIF
animation.save("pattern.gif", writer=PillowWriter(fps=30))

plt.close(fig)

print("Animation saved as pattern.gif")
