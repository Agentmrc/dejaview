import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define time array
t = np.linspace(-1, 5, 2000)

# Define f(t): 5cos(πt)[u(t)-u(t-1)]
f = 5 * np.cos(np.pi * t)
f[(t < 0) | (t > 1)] = 0  # Apply unit step window

# Define h(t): 1.5[u(t)-u(t-1.5)] - [u(t-2)-u(t-2.5)]
h = np.zeros_like(t)
h[(t >= 0) & (t <= 1.5)] = 1.5
h[(t >= 2) & (t <= 2.5)] -= 1

# Compute convolution y(t) = f(t) * h(t)
dt = t[1] - t[0]  # Time step
y = signal.convolve(f, h, mode='full') * dt  # Convolution

# Create time array for convolution result
t_conv = np.linspace(t[0] + t[0], t[-1] + t[-1], len(y))  # Time for convolution result
# Shift to align properly (convolution starts at t_min_f + t_min_h)
t_conv = t_conv - (t[0] * 2)  # Adjust for symmetric convolution

# Alternative: Manual convolution for better understanding
def manual_convolution(t, f, h):
    """Manual convolution implementation"""
    dt = t[1] - t[0]
    y_manual = np.zeros_like(t)
    
    for i, tau in enumerate(t):
        # y(t) = ∫f(τ)h(t-τ)dτ
        h_shifted = np.interp(tau - t, t, h, left=0, right=0)
        y_manual[i] = np.trapz(f * h_shifted, t)
    
    return y_manual

y_manual = manual_convolution(t, f, h)

# Create figure with subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 10))

# Plot f(t)
axes[0].plot(t, f, 'b', linewidth=2, label=r'$f(t) = 5\cos(\pi t)[u(t)-u(t-1)]$')
axes[0].set_xlabel('Time (t)')
axes[0].set_ylabel('Amplitude')
axes[0].set_title('Input Signal: f(t)')
axes[0].grid(True, alpha=0.3)
axes[0].legend()
axes[0].set_xlim([-1, 5])

# Plot h(t)
axes[1].plot(t, h, 'r', linewidth=2, label=r'$h(t) = 1.5[u(t)-u(t-1.5)] - [u(t-2)-u(t-2.5)]$')
axes[1].set_xlabel('Time (t)')
axes[1].set_ylabel('Amplitude')
axes[1].set_title('Impulse Response: h(t)')
axes[1].grid(True, alpha=0.3)
axes[1].legend()
axes[1].set_xlim([-1, 5])

# Plot y(t) using manual convolution (more accurate)
axes[2].plot(t, y_manual, 'g', linewidth=2, label=r'$y(t) = f(t) * h(t)$')
axes[2].set_xlabel('Time (t)')
axes[2].set_ylabel('Amplitude')
axes[2].set_title('Output Signal: y(t)')
axes[2].grid(True, alpha=0.3)
axes[2].legend()
axes[2].set_xlim([-1, 5])

plt.tight_layout()
plt.show()

# Also plot with scipy convolution for comparison
fig2, ax = plt.subplots(figsize=(12, 6))
# Trim convolution result to match original time range
mask = (t_conv >= -1) & (t_conv <= 5)
ax.plot(t_conv[mask], y[mask], 'purple', linewidth=2, label='y(t) using scipy.convolve')
ax.set_xlabel('Time (t)')
ax.set_ylabel('Amplitude')
ax.set_title('Output y(t) (using scipy convolution)')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_xlim([-1, 5])
plt.show()