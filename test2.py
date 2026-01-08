import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define time array
t = np.linspace(-1, 5, 2000)

# Define f(t): 5cos(πt)[u(t)-u(t-1)]
f = 5 * np.cos(np.pi * t)
f[(t < 0) | (t > 1)] = 0

# Define h(t): 1.5[u(t)-u(t-1.5)] - [u(t-2)-u(t-2.5)]
h = np.zeros_like(t)
h[(t >= 0) & (t <= 1.5)] = 1.5
h[(t >= 2) & (t <= 2.5)] -= 1

# Compute convolution numerically
dt = t[1] - t[0]
y_numerical = signal.convolve(f, h, mode='full') * dt
t_conv = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y_numerical))
t_conv = t_conv - (t[0] * 2)  # Adjust time axis
mask = (t_conv >= -1) & (t_conv <= 5)

# Analytical function (with your correction for 2.5 ≤ t < 3)
def y_analytical_corrected(t_val):
    t_val = np.asarray(t_val)
    y = np.zeros_like(t_val)
    
    cond1 = (0 <= t_val) & (t_val < 1)
    cond2 = (1 <= t_val) & (t_val < 1.5)
    cond3 = (1.5 <= t_val) & (t_val < 2)
    cond4 = (2 <= t_val) & (t_val < 2.5)
    cond5 = (2.5 <= t_val) & (t_val < 3)
    cond6 = (3 <= t_val) & (t_val < 3.5)
    
    y[cond1] = (7.5/np.pi) * np.sin(np.pi * t_val[cond1])
    y[cond2] = 0
    y[cond3] = -(7.5/np.pi) * np.sin(np.pi * (t_val[cond3] - 1.5))
    y[cond4] = -(7.5/np.pi) * np.sin(np.pi * (t_val[cond4] - 1.5)) - (5/np.pi) * np.sin(np.pi * (t_val[cond4] - 2))
    y[cond5] = -(5/np.pi) * (np.sin(np.pi * (t_val[cond5] - 2)) - np.sin(np.pi * (t_val[cond5] - 2.5)))
    y[cond6] = (5/np.pi) * np.sin(np.pi * (t_val[cond6] - 2.5))
    
    return y

# Calculate analytical
y_analyt = y_analytical_corrected(t)

# Plot comparison
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

# Numerical convolution
ax1.plot(t_conv[mask], y_numerical[mask], 'b', linewidth=2, label='Numerical convolution')
ax1.set_title('Numerical Convolution (scipy)')
ax1.grid(True, alpha=0.3)
ax1.legend()
ax1.set_xlim([-1, 5])

# Analytical solution
ax2.plot(t, y_analyt, 'r', linewidth=2, label='Analytical solution')
ax2.set_title('Analytical Solution (Corrected)')
ax2.grid(True, alpha=0.3)
ax2.legend()
ax2.set_xlim([-1, 5])

# Difference
ax3.plot(t, y_analyt - np.interp(t, t_conv[mask], y_numerical[mask]), 'g', linewidth=1)
ax3.set_title('Difference (Analytical - Numerical)')
ax3.grid(True, alpha=0.3)
ax3.set_xlim([-1, 5])

plt.tight_layout()
plt.show()

# Print values at key points
print("Comparison at key points:")
print("t = 2.5:")
print(f"  Analytical: {y_analytical_corrected([2.5])[0]:.6f}")
print(f"  Numerical: {np.interp(2.5, t_conv[mask], y_numerical[mask]):.6f}")

print("\nt = 2.7:")
print(f"  Analytical: {y_analytical_corrected([2.7])[0]:.6f}")
print(f"  Numerical: {np.interp(2.7, t_conv[mask], y_numerical[mask]):.6f}")

print("\nt = 2.8:")
print(f"  Analytical: {y_analytical_corrected([2.8])[0]:.6f}")
print(f"  Numerical: {np.interp(2.8, t_conv[mask], y_numerical[mask]):.6f}")

print("\nt = 2.9:")
print(f"  Analytical: {y_analytical_corrected([2.9])[0]:.6f}")
print(f"  Numerical: {np.interp(2.9, t_conv[mask], y_numerical[mask]):.6f}")