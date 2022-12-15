from ast import Assert


def check_odd_or_even(variable):
    if (variable % 2) == 1:
        print("odd")
    else:
        print("even")

def check_list_size(lst):
    return len(lst)

def add_to_list(lst, number):
    lst.append(number)

def sum_of_list(lst):
    _sum = 0
    for num in lst:
        _sum += num
    return _sum

def add_index_to_list(lst):
    new_lst = []
    for index in range(len(lst)):
        new_lst.append(lst[index] + index)
    return new_lst

# Unit tests-------------------------------------
def sum_of_list_unit_test():
    test_lst = [1, 2, 3, 4, 4, 3, 2, 1]
    expectedresult = 20
    actualresult = sum_of_list(test_lst)
    assert(expectedresult == actualresult)

def add_index_to_list_unit_test():
    test_lst = [1, 2, 3]
    expectedresult = [1, 3, 5]
    actualresult = add_index_to_list(test_lst)
    assert(expectedresult == actualresult)

def run_unit_tests():
    sum_of_list_unit_test()
    add_index_to_list_unit_test()
# Unit tests--------------------------------------    


if __name__=="__main__":

    run_unit_tests()

    variable1 = 5
    print(check_odd_or_even(variable1))

    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(check_list_size(lst1))

    add_to_list(lst1, 9)
    print(lst1)

    print(add_index_to_list([1, 2, 3]))










