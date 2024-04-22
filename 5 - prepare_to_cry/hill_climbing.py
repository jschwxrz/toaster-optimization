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
    current_parameters = (random.randint(1,100), random.randint(1,100), random.uniform(0.0,2.0), random.randint(1,10))
    while True:
        next_solution = get_max_neighbor(current_parameters)
        if next_solution is None:
            break
        if utility(*next_solution) > utility(*current_parameters):
            current_parameters = next_solution
        else:
            break
    return current_parameters

def get_max_neighbor(current_parameters):
    original_parameters = current_parameters
    best_parameters = current_parameters
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in [-0.001, 0, 0.001]:
                for l in range(-1, 2):
                    candidate_parameters = (original_parameters[0]+i, original_parameters[1]+j, original_parameters[2]+k, original_parameters[3]+l)
                    if (1 <= candidate_parameters[0] <= 100 and
                        1 <= candidate_parameters[1] <= 100 and
                        0.0 <= candidate_parameters[2] <= 2.0 and
                        1 <= candidate_parameters[3] <= 10):
                        if utility(*candidate_parameters) > utility(*best_parameters):
                            best_parameters = candidate_parameters
    if best_parameters == original_parameters:
        return None
    return best_parameters

optimums = {}
repetitions = 500

for i in range(repetitions):
    print(f"{i+1}/{repetitions}")
    optimum = find_maximum()
    optimums[int(utility(*optimum))] = optimum
sorted_optimums = {k: optimums[k] for k in sorted(optimums)}

filtered_optimums = {}
prev_num = None

for k, v in sorted_optimums.items():
    if prev_num is None or abs(k - prev_num) >= 3:
        filtered_optimums[k] = v
        prev_num = k

for i, v in filtered_optimums.items():
    print(f"Optimum: {v}, \nvalue: {i}") 

