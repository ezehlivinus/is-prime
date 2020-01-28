def is_prime(number):
    def is_even(number):
        return number % 2 == 0
    
    prime = 1
    if( number <= -1 ):
        return False
    elif number in [0, 1]:
        return False
    elif number == 2:
        return True
    elif number > prime:
        try:
            if is_even(number):
                return False
            else:
                # check if it is divisible by other prime numbers
                if number % 3 == 0 and number != 3:
                    return False
                elif number % 5 == 0 and number != 5:
                    return False
                return True
        except:
            raise

for number in range(0, 100):
    if(is_prime(number)):
        print(number, is_prime(number), end=" ")

