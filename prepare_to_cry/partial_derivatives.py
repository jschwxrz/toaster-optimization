import math
import random

def utility(toast_duration, wait_duration, power = 1.0,toaster = 1):
    if (not type(toast_duration) is int):
        raise ValueError("toast_duration is not an integer")
    if not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not in the valid range")
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

def find_maximum(toast_duration, wait_duration, power, toaster):
	
    while True:
        # get gradient by calculating partial derivatives
        next_parameters = get_gradient(toast_duration, wait_duration, power, toaster)
        

        if not 0 < int(next_parameters[0]) <= 100 or not 0 < int(next_parameters[1]) <= 100 or not 0 < next_parameters[2] < 2 or not 0 < next_parameters[3] <= 10:
            break

        if abs(utility(int(next_parameters[0]), int(next_parameters[1]), next_parameters[2], int(next_parameters[3])) - utility(int(toast_duration), int(wait_duration), power, int(toaster))) < 1e-6:
            break

        # reassigning values for next run
        toast_duration = int(next_parameters[0])
        wait_duration = int(next_parameters[1])
        power = next_parameters[2]
        toaster = int(next_parameters[3])
    return int(toast_duration), int(wait_duration), power, toaster


def get_gradient(toast_duration, wait_duration, power, toaster):
    # handling input errors
    if (not type(toast_duration) is int) or not (1 <= toast_duration <= 100):
        raise ValueError("toast_duration is not an integer")
    if (not type(wait_duration) is int) or not (1 <= wait_duration <= 100):
        raise ValueError("wait_duration is not an integer")
    if (not type(power) is float) or not (0.0 <= power <= 2.0):
        raise ValueError("power is not a float or not in the valid range")
    if (not type(toaster) is int) or not (1 <= toaster <= 10):
        raise ValueError("toaster is not an integer or is not in a valid range")
    
    original_parameters = (toast_duration, wait_duration, power, toaster)
    best_parameters = (toast_duration, wait_duration, power, toaster)
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                power_gradient = ((-0.1 * (i - 10) ** 2 + 1) + (-0.01 * (i - 1) ** 2 + 1)) * (10 * math.cos(10 * best_parameters[2] + math.pi/2 - 10) + 0.2)
                new_power = best_parameters[2] + 0.0001 * power_gradient
                candidate_parameters = (original_parameters[0]+i, original_parameters[1]+j, new_power, original_parameters[3]+k)
                if (1 <= candidate_parameters[0] <= 100 and
                    1 <= candidate_parameters[1] <= 100 and
                    0.0 <= candidate_parameters[2] <= 2.0 and
                    1 <= candidate_parameters[3] <= 10):
                    if utility(*candidate_parameters) > utility(*best_parameters):
                        best_parameters = candidate_parameters
    return best_parameters

optimums = {}
repetitions = 500

for i in range(repetitions):
    print(f"{i+1}/{repetitions}")
    optimum = find_maximum(random.randint(1,100), random.randint(1,100), random.uniform(0.0,2.0), random.randint(1,10))
    optimums[int(utility(*optimum))] = optimum
sorted_optimums = {k: optimums[k] for k in sorted(optimums)}

all_optimums = []
for k, v in optimums.items():
    all_optimums.append(k)

all_optimums.sort()
filtered_optimums = []
prev_num = None

for num in all_optimums:
    if prev_num is None or abs(num - prev_num) >= 3:
        filtered_optimums.append(num)
        prev_num = num


print("Optimums with their parameters:")
print(sorted_optimums)
print("Optimums when taking into account an error of 3:")
print(filtered_optimums)