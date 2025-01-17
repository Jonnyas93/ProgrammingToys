#The problem I am solving here can be found at this URL: https://edabit.com/challenge/JzXH3QnwHmpptadQr

def bitwise_logical_negation(num):# Num must be between -2,147,483,647 and 2,147,483,647, as it is a 32-bit signed integer and is needed for the bitwise negation to function correctly
    #Set the sign bit for negative numbers, add 1 to handle the zero case, shift right by 1 to normalize the result to 0 or 1
    return ((num | (num >> 31)) + 1) >> 1

if __name__ == "__main__":
    print(bitwise_logical_negation(1))
    print(bitwise_logical_negation(5))
    print(bitwise_logical_negation(0))
    print(bitwise_logical_negation(3))
    print(bitwise_logical_negation(-3))