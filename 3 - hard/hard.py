import math
import random

def utility(toast_duration, wait_duration, power = 1.0,toaster = 1):
    if (not type(toast_duration) is int) or not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) or not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(toaster) is int) or not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    if (not type(power) is float) or not (0.0 <= power <= 2.0):
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

def find_maximum():
    max_iterations = 1000
    tolerance = 1e-6
    # random starting point
    toast_duration = random.randint(1, 100)
    wait_duration = random.randint(1, 100)
    power = random.uniform(0, 2)
    for _ in range(max_iterations):
        current_utility = utility(toast_duration, wait_duration, power)
        # toast increase / decrease
        plus_toast_duration = min(toast_duration + 1, 100)
        plus = utility(plus_toast_duration, wait_duration, power)
        minus_toast_duration = max(toast_duration - 1, 1)
        minus = utility(minus_toast_duration, wait_duration, power)
        if current_utility > plus and current_utility > minus:
            pass
        elif plus < minus:
            toast_duration = minus_toast_duration
        else:
            toast_duration = plus_toast_duration
        # wait increase / decrease
        plus_wait_duration = min(wait_duration + 1, 100)
        plus = utility(toast_duration, plus_wait_duration, power)
        minus_wait_duration = max(wait_duration - 1, 1)
        minus = utility(toast_duration, minus_wait_duration, power)
        if current_utility > plus and current_utility > minus:
            pass
        elif plus < minus:
            wait_duration = minus_wait_duration
        else:
            wait_duration = plus_wait_duration
        # power increase / decrease
        plus_power = min(power + 1, 2.0)
        plus = utility(toast_duration, wait_duration, plus_power)
        minus_power = max(power - 1, 0.0)
        minus = utility(toast_duration, wait_duration, minus_power)
        if current_utility > plus and current_utility > minus:
            pass
        elif plus < minus:
            power = minus_power
        else:
            power = plus_power
        new_utility = utility(toast_duration, wait_duration, power)
        if abs(current_utility - new_utility) < tolerance:
            break
    return (toast_duration, wait_duration, power)


optimum = find_maximum()
print("Optimum:",optimum,)
print("value:",utility(*optimum))