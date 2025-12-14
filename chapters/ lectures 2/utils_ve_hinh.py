%%writefile utils_ve_hinh.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- HÀM 1: VẼ MÔ HÌNH CON LẮC (SCHEMATIC) ---
def ve_mo_hinh_con_lac():
    fig, ax = plt.subplots(figsize=(6, 6))
    L = 1.0; theta_deg = 30; theta_rad = np.radians(theta_deg)
    pivot = (0, 0); bob_x = L * np.sin(theta_rad); bob_y = -L * np.cos(theta_rad)

    # Trần và trục
    ax.plot([-0.5, 0.5], [0, 0], color='black', linewidth=2)
    for i in np.linspace(-0.5, 0.5, 12): ax.plot([i, i + 0.1], [0, 0.1], color='black', linewidth=1)
    ax.add_patch(patches.Arc((0, 0), 0.1, 0.1, theta1=180, theta2=360, color='black', linewidth=2))
    ax.plot([0, 0], [0, -L * 1.3], color='black', linestyle='--', linewidth=1)
    ax.plot([0, bob_x], [0, bob_y], color='black', linewidth=2.5) # Dây

    # Quả nặng
    circle = patches.Circle((bob_x, bob_y), radius=0.08, facecolor='#A52A2A', edgecolor='black', zorder=5)
    ax.add_patch(circle)

    # Ký hiệu
    ax.add_patch(patches.Arc((0, 0), 0.5, 0.5, theta1=270, theta2=270+theta_deg, color='black'))
    ax.annotate('', xy=(0.12, -0.22), xytext=(0.02, -0.25), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='black'))
    ax.text(0.1, -0.2, r'$\theta$', fontsize=16, va='center')
    ax.text(bob_x / 2 + 0.05, bob_y / 2, r'$l$', fontsize=16)
    ax.text(bob_x, bob_y - 0.15, r'$m$', fontsize=16, ha='center')
    
    # Trọng trường g
    ax.arrow(-0.3, -0.5, 0, -0.2, head_width=0.03, head_length=0.05, fc='black', ec='black')
    ax.text(-0.38, -0.6, r'$g$', fontsize=16)

    ax.set_aspect('equal'); ax.axis('off')
    plt.figtext(0.5, 0.05, 'Figure 2.1 - The simple pendulum', ha='center', fontsize=12, fontname='serif')
    plt.show()

# --- HÀM 2: VẼ ĐỒ THỊ PHA OVERDAMPED ---
def ve_do_thi_overdamped():
    x = np.linspace(-2.5 * np.pi, 2.5 * np.pi, 1000)
    A = 2.0; y = -A * np.sin(x)
    fig, ax = plt.subplots(figsize=(10, 5))

    # Trục
    ax.axhline(0, color='black', linewidth=1)
    ax.arrow(2.5 * np.pi + 0.3, 0, 0.2, 0, head_width=0.2, fc='black', ec='black', clip_on=False)
    ax.text(2.5 * np.pi + 0.6, 0.2, r'$x$', fontsize=16, va='center')
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.arrow(0, A + 0.5, 0, 0.2, head_width=0.15, fc='black', ec='black', clip_on=False)
    ax.text(0.3, A + 0.8, r'$\dot{x}$', fontsize=18, ha='left', fontweight='bold')

    # Đồ thị và điểm cân bằng
    ax.plot(x, y, color='black', linewidth=2.5)
    ax.plot([-2*np.pi, 0, 2*np.pi], [0, 0, 0], 'o', color='black', markersize=10, zorder=10) # Stable
    ax.plot([-np.pi, np.pi], [0, 0], 'o', mfc='white', mec='black', mew=2, markersize=10, zorder=10) # Unstable

    # Mũi tên dòng chảy
    arrow_pos = [(-2.25*np.pi, '>'), (-1.5*np.pi, '<'), (-0.5*np.pi, '>'), (0.5*np.pi, '<'), (1.5*np.pi, '>'), (2.25*np.pi, '<')]
    for pos, marker in arrow_pos: ax.plot(pos, 0, marker=marker, color='black', markersize=8)

    # Chú thích biên độ
    ax.plot([-0.1, 0.1], [A, A], color='black', linewidth=1)
    ax.text(0.2, A, r'$\frac{mgl}{b}$', fontsize=16, va='center')
    
    ax.axis('off'); ax.set_xlim(-2.5*np.pi - 0.5, 2.5*np.pi + 1.0); ax.set_ylim(-A - 1, A + 1.5)
    plt.tight_layout(); plt.show()

# --- HÀM 3: VẼ ĐỒ THỊ MEMORY LATCHING ---
def ve_do_thi_memory():
    dt = 0.01; t = np.arange(0, 30.1, dt); n = len(t)
    x = np.zeros(n); u = np.zeros(n)
    x[0] = 0.1; w = 2.0
    u[(t >= 10) & (t < 20)] = -5.0
    
    for i in range(n - 1):
        dxdt = -x[i] + np.tanh(w * x[i]) + u[i]
        x[i+1] = x[i] + dxdt * dt

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    ax1.plot(t, u, label='u(t)', color='#1f77b4'); ax1.set_ylabel('u(t)'); ax1.set_yticks([0, -5]); ax1.legend(loc='lower left'); ax1.grid(True, linestyle=':', alpha=0.6)
    ax2.plot(t, x, label='x(t)', color='#1f77b4'); ax2.set_ylabel('x(t)'); ax2.set_xlabel('time (s)'); ax2.set_yticks([-1, 0, 1]); ax2.legend(loc='upper right'); ax2.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout(); plt.show()
