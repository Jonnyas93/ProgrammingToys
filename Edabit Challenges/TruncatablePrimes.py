# Function to check if a number is a truncatable prime
def truncatable_primes(num):
    # Check if the number is truncatable from the left
    left = left_check(num)
    # Check if the number is truncatable from the right
    right = right_check(num)
    
    # Determine the type of truncatable prime
    if left == True and right == True:
        return "both"
    elif left == True and right == False:
        return "Left"
    elif right == True and left == False:
        return "Right"
    else:
        return False

# Function to check if a number is a left truncatable prime
def left_check(num):
    for i in range(len(str(num))):
        # If any digit is '0', it's not a truncatable prime
        if str(num)[i] == "0":
            return False
        else:
            # Check if the remaining part of the number is prime, accounting for the last digit
            if i == len(str(num)):
                if is_prime(int(str(num)[i])) == False:
                    return False
            else:
                index = i
                if is_prime(int(str(num)[index:])) == False:
                    return False
    return True

# Function to check if a number is a right truncatable prime
def right_check(num):
    for i in range(len(str(num))-1,0,-1):
        # If any digit is '0', it's not a truncatable prime
        if str(num)[i] == "0":
            return False
        else:
            # Check if the remaining part of the number is prime, accounting for the first digit
            if i == 0:
                if is_prime(int(str(num)[i])) == False:
                    return False
            else:
                if is_prime(int(str(num)[:i])) == False:
                    return False
    return True

def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n == 2 or n == 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisibility from 5 to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Increment by 6 to skip even numbers and multiples of 3

    return True

if __name__ == "__main__":
    print(truncatable_primes(9137))
    print(truncatable_primes(5939))
    print(truncatable_primes(317))
    print(truncatable_primes(5))
    print(truncatable_primes(139))
    print(truncatable_primes(103))