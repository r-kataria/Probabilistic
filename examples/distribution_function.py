import probabilistic


@probabilistic.function(0.5)
def a():
    return 5


@probabilistic.function(0.5)
def b():
    return -5


@probabilistic.distribution_function(n=50000)
def probabilisticSum():
    value_sum = 0
    
    value_a = a()
    value_b = b()
    
    if value_a != None:
        value_sum = value_sum + value_a
    
    if value_b != None:
        value_sum = value_sum + value_b
    
    return value_sum

print(probabilisticSum())