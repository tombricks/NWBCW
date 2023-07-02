import math
class state_categories:
    wasteland = 0
    rural = 1
    town = 2
    large_town = 3
    city = 4
    large_city = 5
    metropolis = 6
    megalopolis = 7

ssstates = {
    1: (state_categories.rural, 5000),
    2: (state_categories.town, 35000),
    3: (state_categories.town, 75500),
    4: (state_categories.large_town, 117500),
    5: (state_categories.large_town, 137500),
    6: (state_categories.large_town, 157500),
    7: (state_categories.city, 700000),
    8: (state_categories.large_city, 1500000),
}

def generate(target, states):
    median = states[math.ceil((len(states)-1)/2)][1]
    weights = {}
    total = 0
    for state in states:
        weights[state] = states[state][0] ** 0.8
        d = math.sqrt(states[state][1]) / math.sqrt(median)
        weights[state] *= d
        total += weights[state]
    mu = target/total
    out = {}
    for state in states:
        out[state] = round(weights[state]*mu)
    return out

out = generate(180, ssstates)
print("180 target factories")
for state in out:
    print(out[state])
