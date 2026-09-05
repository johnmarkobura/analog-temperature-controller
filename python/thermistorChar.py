import numpy as np
import matplotlib.pyplot as plt

# Experimental thermistor data

temperature = np.array([74.7, 90.4])   # degrees Fahrenheit
resistance = np.array([569, 435])      # ohms

# Linear regression
# R(T) = mT + b

m, b = np.polyfit(temperature, resistance, 1)

print(f"Slope: {m:.5f} ohm/°F")
print(f"Intercept: {b:.5f} ohm")

# Generate temperatures for the fitted line
T_fit = np.linspace(72, 93, 200)

# Calculate corresponding resistance values
R_fit = m * T_fit + b

# Plot
plt.figure(figsize=(8, 5))

# Experimental points
plt.scatter(
    temperature,
    resistance,
    s=80,
    label="Measured data"
)

# Linear fit
plt.plot(
    T_fit,
    R_fit,
    linewidth=2,
    label="Linear fit"
)

# Axis labels
plt.xlabel("Temperature (°F)", fontsize=12)
plt.ylabel("Thermistor Resistance (Ω)", fontsize=12)

# Title
plt.title(
    "NTC Thermistor Temperature-Resistance Characterization",
    fontsize=14
)

# Equation displayed on graph
equation = f"$R_T = {m:.5f}T + {b:.5f}$"

plt.text(
    75,
    455,
    equation,
    fontsize=11
)

# Grid and legend
plt.grid(True, alpha=0.3)
plt.legend()

# Clean layout
plt.tight_layout()

# Save figure 
plt.savefig(
    "thermistor_characterization.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()