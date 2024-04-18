import numpy as np
import matplotlib.pyplot as plt
import math

def utility(toast_duration, wait_duration, power = 1.0,toaster = 1):
    if (not type(toast_duration) is int) and not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) and not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(toaster) is int) and not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    if (not type(power) is float) and not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")

    hpt = [10,8,15,7,9,2,9,19,92,32][toaster-1]
    hpw = [1,4,19,3,20,3,1,4,1,62][toaster-1]
    toaster_utility = [1,0.9,0.7,1.3,0.3,0.8,0.5,0.8,3,0.2][toaster-1]

    toast_utility = -0.1*(toast_duration-hpt)**2+1
    wait_utility = -0.01*(wait_duration-hpw)**2+1
    overall_utility = (toast_utility + wait_utility) * toaster_utility

    power_factor = math.sin(10*power+math.pi/2 -10) + power*0.2
    overall_utility *= power_factor

    return overall_utility

def plot_4d():
    toast_time = np.arange(0, 101, 1)
    wait_time = np.arange(0, 101, 1)
    power = np.arange(0, 2, 0.1)

    X, Y, Z = np.meshgrid(toast_time, wait_time, power)

    utility_values = np.zeros_like(X, dtype=float)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            for k in range(X.shape[2]):
                utility_values[i, j, k] = utility(int(X[i, j, k]), int(Y[i, j, k]), Z[i, j, k])

    X_flat = X.flatten()
    Y_flat = Y.flatten()
    Z_flat = Z.flatten()
    utility_flat = utility_values.flatten()

    fig = plt.figure(figsize=(14, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(X_flat, Y_flat, Z_flat, c=utility_flat, cmap="viridis")

    ax.set_xlabel('X: Toast Time')
    ax.set_ylabel('Y: Wait Time')
    ax.set_zlabel('Z: Power')
    fig.colorbar(scatter, label='Utility')

    plt.show()

plot_4d()