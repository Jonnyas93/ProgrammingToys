def truncatable_primes(num):
    left = left_check(num)
    right = right_check(num)
    if left == True and right == True:
        return "both"
    elif left == True and right == False:
        return "Left"
    elif right == True and left == False:
        return "Right"
    else:
        return False

def left_check(num):
    for i in range(len(str(num))):
        if str(num)[i] == "0":
            return False
        else:
            if i == len(str(num)):
                return is_prime(int(str(num)[i]))
            else:
                index = i
                return is_prime(int(str(num)[index:]))

def right_check(num):
    for i in range(len(str(num))-1,0,-1):
        if str(num)[i] == "0":
            return False
        else:
            if i == 0:
                return is_prime(int(str(num)[i]))
            else:
                return is_prime(int(str(num)[:i]))

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