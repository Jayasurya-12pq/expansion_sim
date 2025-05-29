import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

def animate_expansion(L0, dT, alpha, material):
    dL = alpha * L0 * dT
    L_final = L0 + dL

    fig, ax = plt.subplots(figsize=(8, 2))
    ax.set_xlim(0, L_final * 1.2)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Initial rectangle bar
    bar = Rectangle((0, 0.3), L0, 0.4, color='blue')
    ax.add_patch(bar)
    title = ax.text(0.5 * L_final, 0.8, '', ha='center', fontsize=12)

    # Color interpolation: blue (cool) to red (hot)
    def interpolate_color(step, total_steps):
        r = step / total_steps
        b = 1 - r
        return (r, 0.2, b)

    def update(frame):
        current_length = L0 + (dL * frame / 100)
        bar.set_width(current_length)
        bar.set_color(interpolate_color(frame, 100))
        title.set_text(f"{material} expands to {current_length:.4f} m")

    ani = animation.FuncAnimation(fig, update, frames=101, interval=30, repeat=False)
    plt.title(f"Thermal Expansion of {material}", fontsize=14)
    plt.tight_layout()
    plt.show()
