import math

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
    current_parameters = (0,0)
    while True:
        next_solution = get_max_neighbor(current_parameters)
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
            current_parameters = (original_parameters[0]+i, original_parameters[1]+j)
            if utility(*current_parameters) > utility(*best_parameters):
                best_parameters = current_parameters
    return best_parameters

optimum = find_maximum()
print("Optimum:",optimum,)
print("value:",utility(*optimum))