import math
import sys
import io

def lcm(num1, num2):
    #Takes the absolute value of the product of the two numbers and floor divides it by the greatest common divisor of the two numbers to get the least common multiple
    return abs(num1 * num2) // math.gcd(num1, num2)

def lcm_multiple(nums):
    if not nums: #check that nums has been passed
        return None
    result = nums[0]#initialize result to the first number in the list
    for num in nums[1:]:#iterate through the list of numbers and find the least common multiple of all the numbers
        result = lcm(result, num)
    print(result)

if __name__ == "__main__":
    lcm_multiple([1, 2, 3, 4, 5, 6, 7, 8, 9])
    lcm_multiple([5])
    lcm_multiple([5, 7, 11])
    lcm_multiple([5, 7, 11, 35, 55, 77])

#Old bad approach to solve the problem, had very poor time complexity
""" lcm = None
    test = 1
    finalNum = nums[-1]
    while lcm is None:
        test+=1
        print('---------New Test---------')
        for num in nums:
            print(test,'%', num , ' = ', test % num)
            if test % num != 0:
                break
            else:
                if num == finalNum:
                    lcm = test
    print(lcm) """