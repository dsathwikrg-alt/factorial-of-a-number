import sys
import sysconfig


# Algorithm is ::

# 1. Define a function with an appropriate naming convention that accepts integer 'N' from the User
# 2. The defined function will return an Integer
# 3. Iterates over the loop till the time given integer becomes 1 or 0
# 4. Print the Factorial of a given number as a result
# 5. Eg: 5! = 5*4*3*2*1

def num_factorial_iterative(input_num: int) -> int:

    print("input_num is: " + str(input_num))

    if input_num<0:
        error_msg= "Error: Number given is less than 0."
        return error_msg
    else:    

        result = 1
        for i in range(1, input_num+1):
            result *= i

        return result

def main():

    input_num = int(input("Enter the Number : "))

    result = num_factorial_iterative(input_num)
    print("The factorial of a number is :" + str(result))

if __name__ == '__main__':
    main()




