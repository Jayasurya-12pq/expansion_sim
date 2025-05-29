import tkinter as tk
from tkinter import ttk, messagebox
from expansion_sim_animation import animate_expansion  # Import the animation function

# Thermal expansion coefficients (1/°C)
MATERIALS = {
    "Aluminum": 23e-6,
    "Copper": 17e-6,
    "Steel": 12e-6,
    "Brass": 19e-6,
    "Glass": 9e-6
}

def on_calculate():
    try:
        material = material_var.get()
        L0 = float(length_entry.get())
        dT = float(temp_entry.get())
        if L0 <= 0:
            raise ValueError("Length must be positive.")

        alpha = MATERIALS[material]
        animate_expansion(L0, dT, alpha, material)

    except ValueError as e:
        messagebox.showerror("Invalid input", f"Please enter valid numbers.\n{str(e)}")

# GUI Setup
root = tk.Tk()
root.title("ThermoSim - Thermal Expansion Simulator")

tk.Label(root, text="Select Material:").grid(row=0, column=0, padx=10, pady=5)
material_var = tk.StringVar(value="Aluminum")
material_menu = ttk.Combobox(root, textvariable=material_var, values=list(MATERIALS.keys()), state="readonly")
material_menu.grid(row=0, column=1, pady=5)

tk.Label(root, text="Initial Length (m):").grid(row=1, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Temperature Change (°C):").grid(row=2, column=0, padx=10, pady=5)
temp_entry = tk.Entry(root)
temp_entry.grid(row=2, column=1, pady=5)

calc_btn = tk.Button(root, text="Calculate & Animate", command=on_calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
