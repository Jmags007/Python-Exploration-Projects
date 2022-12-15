#list.append(x)
#Adds item to the end of the list
def _append(lst, x):
    count = 0
    #determine length of new list and initializing a new list of size n + 1
    for i in range(len(lst)): 
        count += 1
    new_lst = [None] * (count + 1)

    #copying the original elements unless were at the last spot where we insert x
    for i in range(len(new_lst)):
        if i == (len(new_lst) -1):
            new_lst[i] = x
            break
        new_lst[i] = lst[i]

    return new_lst

#list.extend(iterable)
#adds iterable like another list to the end of the list
def _extend(lst1, lst2):
    '''
    new_lst = [None] * (len(lst1) + len(lst2))
    count = 0
    lst2_flag = False
    for i in range(len(new_lst)):
        if lst2_flag == False:
            new_lst[i] = lst1[i]
            count += 1
            if count == len(lst1):
                lst2_flag = True
        else:
            new_lst[i] = lst2[i - len(lst1)]
        return new_lst
    '''
    for val in lst2:
        lst1.append(val)

    return lst1



#list.insert(i, x)
#inserts item x into the specified index
def _insert(lst, index, x):
    new_lst = [None] * len(lst)
    for i in range(len(lst)):
        if i == index:
            new_lst[i] = x
        else:
            new_lst[i] = lst[i]
    return new_lst

#list.remove(x)
#removes the first item that matches x
def _remove(lst, x):
    new_lst = [None] * (len(lst) - 1)
    flag = False
    for i in range(len(new_lst)):
        if lst[i] == x and flag == False:
            flag = True

        if flag == False:
            new_lst[i] = lst[i]
        else:
            new_lst[i] = lst[(i + 1)]
    return new_lst


#list.pop([i])
#removes the item at index i
def _pop(lst, x):
    new_lst = [None] * (len(lst) - 1)
    flag = False
    for i in range(len(new_lst)):
        if i == x:
            flag = True
        if flag == False:
            new_lst[i] = lst[i]
        else:
            new_lst[i] = lst[i + 1]
    
    return new_lst

#list.clear()
#clears the list so that the object is None
def _clear(lst):
    new_lst = None

    return new_lst

#list.index(x[, start[, end]])
#determine the index of where x is in the list
def _index(lst, x):
    index = None
    for i, val in enumerate(lst):
        if val == x:
            index = i
    if index == None:
        raise ValueError
    return index


#list.count(x)
#counts how many items of x are in list
def _count(lst, x):
    count = 0
    for val in lst:
        if val == x:
            count += 1
    return count

#list.sort(*, key=None, reverse=False)
#sorts the string from lowest to highest
def _sort(lst):
    new_lst = []
    sort_lst = [None] * len(lst)
    for i, val in enumerate(lst):
        sort_lst[i] = val
    min_val_index = 0
    flag = True
    while flag == True:
        for i, val in enumerate(sort_lst):
            if i == 0:
                min_value = val
                min_val_index = i
            if min_value > val:
                min_value = val
                min_val_index = i
        new_lst.append(sort_lst[min_val_index])
        sort_lst.pop(min_val_index)
        if sort_lst == []:
            flag = False
    return new_lst
            

#list.reverse()
#reverses a list
def _reverse(lst):
    new_lst = [None] * len(lst)
    for i, val in enumerate(lst):
        new_lst[-i -1] = val
    return new_lst

#list.copy()
#makes a shallow copy
def _copy(lst):
    new_lst = [None] * len(lst)
    for i in range(len(lst)):
        new_lst[i] = lst[i]
    return new_lst

#unit tests---------------------------------------
def run_unit_tests():
    _append_unit_test()
    _extend_unit_test()
    _insert_unit_test()
    _remove_unit_test1()
    _remove_unit_test2()
    _pop_unit_test()
    _clear_unit_test()
    _count_unit_test()
    _reverse_unit_test()
    _copy_unit_test()
    _index_unit_test()
    _sort_unit_test()

def _append_unit_test():
    test_lst = [1,2,3]
    test_parm = "a"
    expectedresult = [1,2,3,"a"]
    actualresult = _append(test_lst, test_parm)
    assert(expectedresult == actualresult)

def _extend_unit_test():
    test_lst1 = ["apple", "banana", "cherry"]
    test_lst2 = ["tesla", "BMW", "Ford"]
    expectedresult = ["apple", "banana", "cherry", "tesla", "BMW", "Ford"]
    actualresult = _extend(test_lst1, test_lst2)
    assert(expectedresult == actualresult)

def _insert_unit_test():
    test_lst = [1, 2, 3]
    test_index = 1
    test_x = "z"
    expectedresult = [1, "z", 3]
    actualresult = _insert(test_lst, test_index, test_x)
    assert(expectedresult == actualresult)

def _remove_unit_test1():
    test_lst = [1, 2, 3, 4, 5]
    test_x = 3
    expectedresult = [1, 2, 4, 5]
    actualresult = _remove(test_lst, test_x)
    assert(expectedresult == actualresult)

def _remove_unit_test2():
    test_lst = [1, 2, 3, 3, 5]
    test_x = 3
    expectedresult = [1, 2, 3, 5]
    actualresult = _remove(test_lst, test_x)
    assert(expectedresult == actualresult)

def _pop_unit_test():
    test_lst = [1, 2, 3, 4, 5]
    test_x = 2
    expectedresult = [1, 2, 4, 5]
    actualresult = _pop(test_lst, test_x)
    assert(expectedresult == actualresult)

def _clear_unit_test():
    test_lst = [1, 2, 3, 4, 5]
    expectedresult = None
    actualresult = _clear(test_lst)
    assert(expectedresult == actualresult)

def _count_unit_test():
    test_lst = [1, 2, 3, 3, 4, 5]
    test_x = 3
    expectedresult = 2
    actualresult = _count(test_lst, test_x)
    assert(expectedresult == actualresult)

def _reverse_unit_test():
    test_lst = [1, 2, 3, 4, 5]
    expectedresult = [5, 4, 3, 2, 1]
    actualresult = _reverse(test_lst)
    assert(expectedresult == actualresult)

def _copy_unit_test():
    test_lst = [1, 2, 3, 3, 4, 5]
    expectedresult = [1, 2, 3, 3, 4, 5]
    actualresult = _copy(test_lst)
    assert(expectedresult == actualresult)

def _index_unit_test():
    test_lst = [1, 2, 3, 4, 5, 6, 7]
    test_x = 3
    expectedresult = 2
    actualresult = _index(test_lst, test_x)
    assert(expectedresult == actualresult)

def _sort_unit_test():
    test_lst = [2, 4, 6, 3, 5, 8, 7, 9, 1]
    expectedresult = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actualresult = _sort(test_lst)
    assert(expectedresult == actualresult)


#end of unit tests--------------------------------



if __name__=="__main__":

    run_unit_tests()

    print(_append([1,2,3], "a"))
    print(_extend(["hi", "hello", "yo"], ["me", "myself", "I"]))
    print(_insert([3, 2, 2, 1], 1, "yo"))
    print(_remove([1, 2, 3, 4, 5], 4))
    print(_pop([1, 2, 3, 4, 5], 3))
    print(_clear([1, 2, 3, 4, 5]))
    print(_count([1, 2, 2, 2, 2, 3, 4], 2))
    print(_reverse([1, 5, 2, 3, 7, 8, 8, 9]))
    print(_copy([1, 2, 3, 3, 4, 5]))
    print(_index([1, 2, 3, 3, 3, 3, 3, 4, 5], 4))
    print(_sort([9, 8, 8, 3, 3, 5, 6, 4, 2, 1, 1]))



    