import numpy as np
import matplotlib.pyplot as plt

def PosisiGLB(t):
    v0 = 10  # kecepatan awal
    x0 = 0   # posisi awal
    a = 2    # percepatan (diubah dari g ke nilai konstan)

    # Posisi pada GLB: x(t) = x0 + v0 * t + (1/2) * a * t^2
    x = x0 + v0 * t + 0.5 * a * t**2

    # Kecepatan pada GLB: v(t) = v0 + a * t
    v = v0 + a * t

    data = f"{t}; {round(x, 2)}; {round(v, 2)}\n"
    
    print(data)

    with open("data_GL.txt", "a") as file:
        file.write(data)

    '''
    # Uncomment the following section if you want to plot the position-time and velocity-time graphs
    t_values = np.arange(0.0, T, 0.01)
    x_values = x0 + v0 * t_values + 0.5 * a * t_values**2
    v_values = v0 + a * t_values

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Position (m)', color=color)
    ax1.plot(t_values, x_values, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Velocity (m/s)', color=color)
    ax2.plot(t_values, v_values, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('Position and Velocity vs Time for GLB')
    plt.show()
    '''

print('t , x , v')
with open("data_GL.txt", "w") as file:
    file.write("t; Position; Velocity\n")

for i in range(0, 25):
    t = 0.1 * i
    PosisiGLB(round(t, 2))
