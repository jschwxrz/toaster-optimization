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

def find_maximum(toast_duration, wait_duration, power):
    learning_rate = 0.01
    learning_rate_power = 0.00001
	
    while True:
        # get gradient by calculating partial derivatives
        toast_duration_gradient, wait_duration_gradient, power_gradient = get_gradient(toast_duration, wait_duration, power)
        
        # calculating the next points
        toast_duration_next = toast_duration + learning_rate * toast_duration_gradient
        wait_duration_next = wait_duration + learning_rate * wait_duration_gradient
        power_next = power + learning_rate_power * power_gradient

        if  abs(utility(int(toast_duration_next), int(wait_duration_next), power_next) - utility(toast_duration, wait_duration, power)) < 1e-6:
            break

        # reassigning values for next run
        toast_duration = int(toast_duration_next)
        wait_duration = int(wait_duration_next)
        power = power_next
    return int(toast_duration), int(wait_duration), power


def get_gradient(toast_duration, wait_duration, power):
    # handling input errors
    if (not type(toast_duration) is int) or not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) or not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(power) is float) or not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")

    # calculating derivatives
    toast_duration_gradient = (-0.2 * toast_duration + 2) * (math.sin(10 * power + math.pi / 2 - 10) + power * 0.2)
    wait_duration_gradient = (-0.02 * wait_duration + 0.02) * (math.sin(10 * power + math.pi / 2 - 10) + power * 0.2)
    power_gradient = ((-0.1 * (toast_duration - 10) ** 2 + 1) + (-0.01 * (wait_duration - 1) ** 2 + 1)) * (10 * math.cos(10 * power + math.pi/2 - 10) + 0.2)

    return toast_duration_gradient, wait_duration_gradient, power_gradient

optimum = find_maximum(random.randint(1,100), random.randint(1,100), random.uniform(0.0,2.0))
print("Optimum:",optimum)
print("value:",utility(*optimum))