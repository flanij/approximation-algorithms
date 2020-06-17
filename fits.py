def firstFit(capacity, items, weights):
    bins_used = 0
    bins = [capacity] * items


    # Loop through each item
    for i in range(items):
        j = 0
        # look for a compatible bin
        while(j < bins_used):
            if(bins[j] >= weights[i]):
                bins[j] = bins[j] - weights[i]
                break
            j += 1
        # no campatible bin, start a new one
        if(j == bins_used):
            bins[bins_used] = capacity - weights[i]
            bins_used += 1

    return bins_used

def firstFitDecreasing(capacity, items, weights):
    return firstFit(capacity, items, sorted(weights, reverse=True))

def bestFit(capacity, items, weights):
    bins_used = 0
    bins = [capacity] * items


    # loop through each items
    for i in range(items):
        j = 0
        min = capacity
        idx = 0
        # find the tightest possible bin
        while(j < bins_used):
            if(bins[j] >= weights[i] and bins[j] - weights[i] <= min):
                idx = j
                min = bins[j] - weights[i]
            j += 1
        # no bins available start a new one
        if(min == capacity):
            bins[bins_used] = capacity - weights[i]
            bins_used += 1
        # place item in tightest fitting bin
        else:
            bins[idx] -= weights[i]

    return bins_used