

def is_prime(integer: int) -> bool:
    """Function to check if an integer is a prime"""
    if integer < 1:
        return False

    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True
