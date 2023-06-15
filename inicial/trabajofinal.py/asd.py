EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    return (EXPECTED_BAKE_TIME - elapsed_bake_time)
    
  
def preparation_time_in_minutes(number_of_layers):
    return (number_of_layers*2)
    

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    a = preparation_time_in_minutes(number_of_layers)
    b = (elapsed_bake_time)
    print (a + b)

elapsed_time_in_minutes(1,3)