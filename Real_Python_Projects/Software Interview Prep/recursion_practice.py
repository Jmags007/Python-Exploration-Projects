#write a recursive funciton that given an input n sums all nonnegative interger up to n.
#ex: sum(4) => (1+2+3+4) => 10
#ex: sum(n) => (1+2+3+...+ n)

def recursive_func(n):
    if n == 0:
        return 0
    else:
        return n + recursive_func(n-1)


#takes in binary sting, iterates through and calculates the base 10 number

# 1 10 100 1000
# 327   = 7 * 1 + 2 * 10 + 3*100 = 7 * 10^0 + 2 * 10^1 + 3 * 10^2

# 1 2 4 8 16 32 64
#1001 = 1 * 2^0 + 0 * 2^1 + 0 * 2^2 + 1 * 2^3 = 9
# 11011 = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 + 1 * 2^4
#            1         2        0         8          16 = 27
# 10100 =0 * 2^0 + 0 * 2^1 + 1 * 2^2 + 0 * 2^3 + 1 * 2^4
#            0        0          4        0         16 = 20
#reason for using these voltage going through gates can be respresnet in base system 2

#write a interative soutlino to calculate binary
def binary_iterative(string):
    string_sum = 0
    count = 0
    #iterate from right to left
    for i in range(len(string)-1, -1, -1):
        string_sum += int(string[i]) * (2 ** count)
        count += 1
    return string_sum

#write the fibonacci program recursively
#n = 6 ===> 0, 1, 1, 2, 3, 5
def fibonacci_recursion(n):
    #starting conditions
    if n == 0:
        return 1
    elif n == 1:   
        return 1
    #check if n has been calculated
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

#homework-----------------------------sesh 5----------------------------------
#try different numbers
# 1, 2, 3, 4, 5, 6, 7,  
# 1, 1, 2, 3, 5, 8, 13,
memo_nums = {}
def memo_fibonacci_recursion(n):
    #base case check
    if n <= 1:
        return 1
    #if fib num already calculated return value
    if n in memo_nums:
        return memo_nums[n]
    #if fib num not caculated yet, calculate and put in dic
    else:
        fib_num = memo_fibonacci_recursion(n-1) + memo_fibonacci_recursion(n-2)
        memo_nums[n] = fib_num
        return fib_num

#factorial calcuilator:
# 4! => 4x3x2x1 = 24
factorial_nums = {}
def factorial_calculator(n):
    #base case
    if n == 1:
        return 1
    
    if n in factorial_nums:
        print("ya made it here")
        return factorial_nums[n]
    else:
        factorial_num = n*factorial_calculator(n-1)
        factorial_nums[n] = factorial_num
        return factorial_num
        


# end of session 5 homework----------------------------------------------------------

def binary_recursion(string, n=1):
    if len(string) == 0:
        return 0
    else:
        return (int(string[-1]) * n) + binary_recursion(string[:-1], n*2)
    
    '''
    if len(string) == 0:
        return 0
    else:
        #start from left to right using high order multiple to lowest
        return int(string[0]) * (2 ** (len(string) - 1)) + binary_recursion(string[1:])
    '''



def unit_tests():
    binary_iteratrive_unit_test()
    binary_recursion_unit_test()
    fibonacci_recursion_unit_test()
    memo_fibonacci_recursion_unit_test()
    factorial_calculator_unit_test()

def binary_iteratrive_unit_test():
    test_string = "11011"
    expectedresult = 27
    actualresult = binary_iterative(test_string)
    assert(expectedresult == actualresult)

def binary_recursion_unit_test():
    test_string = "11011"
    expectedresult = 27
    actualresult = binary_recursion(test_string)
    assert(expectedresult == actualresult)

def fibonacci_recursion_unit_test():
    test_n = 6
    expectedresult = 13
    actualresult = fibonacci_recursion(test_n)
    assert(actualresult == expectedresult)

def memo_fibonacci_recursion_unit_test():
    test_n = 6
    expectedresult = 13
    actualresult = memo_fibonacci_recursion(test_n)
    assert(actualresult == expectedresult)

def factorial_calculator_unit_test():
    test_n = 4
    expectedresult = 24
    actualresult = factorial_calculator(test_n)
    assert(actualresult == expectedresult)

#1,1,2,3,5,8,13
#0,1,2,3,4,5,6,7

if __name__ == "__main__":

    unit_tests()

    #print(binary_iterative('110010100110101'))
    #print(binary_recursion('110010100110101'))


    print(fibonacci_recursion(30))
    print(memo_fibonacci_recursion(31))
   # string[0:-1]

    print(factorial_calculator(4))

'''
    s = "abc123"

    sum_of_n = recursive_func(3)
    print(sum_of_n)
'''