import yatzee_game as yat

#go through this file and put yat in for all of the functions that are called form that yazee game file

#unit tests-------------------------------------------
#roll_dice unit test
def unit_tests():
    roll_dice_is_int_unit_test()
    upper_scoring_unit_test()
    three_of_a_kind_scoring_unit_test()
    four_of_a_kind_scoring_unit_test()
    full_house_scoring_unit_test()
    small_straight_unit_test()
    large_straight_unit_test()
    chance_unit_test()
    yahtzee_scoring_unit_test()

def roll_dice_is_int_unit_test():
    exepctedresult = [True, True, True, True, True]
    actual_result = []
    dice_roll = yat.roll_dice(5)
    for i in dice_roll:
        if i > 0 and i < 7 and type(i) == int:
            actual_result.append(type(i) == int)
    assert(actual_result == exepctedresult)

def upper_scoring_unit_test():
    test_lst = [1, 2, 2, 3, 4]
    test_numb = 2
    expectedresult = 4
    actualresult = yat.upper_scoring(test_lst, test_numb)
    assert(expectedresult == actualresult)

def three_of_a_kind_scoring_unit_test():
    test_lst = [1, 2, 2, 2, 3]
    expectedresult = 10
    actualresult = yat.three_of_a_kind_scoring(test_lst)
    assert(actualresult == expectedresult)

def four_of_a_kind_scoring_unit_test():
    test_lst = [6, 2, 2, 2, 2]
    expectedresult = 14
    actualresult = yat.four_of_a_kind_scoring(test_lst)
    assert(actualresult == expectedresult)

def full_house_scoring_unit_test():
    test_lst = [3, 4, 3, 3, 4]
    expectedresult = 25
    actualresult = yat.full_house_scoring(test_lst)
    assert(expectedresult == actualresult)

def small_straight_unit_test():
    test_lst = [3, 2, 2, 1, 4]
    expectedresult = 30
    actualresult = yat.small_straight_scoring(test_lst)
    assert(expectedresult == actualresult)
#test for small straight 

#think about all edge cases


def large_straight_unit_test():
    test_lst = [2, 1, 3, 4, 5]
    expectedresult = 50
    actualresult = yat.large_straight_scoring(test_lst)
    assert(expectedresult == actualresult)

def chance_unit_test():
    test_lst = [2,5,3,4,1]
    expectedreseult = 15
    actualresult = yat.chance_scoring(test_lst)
    assert(expectedreseult == actualresult)

def yahtzee_scoring_unit_test():
    test_lst = [1,1,1,1,1]
    expected_result = 50
    actualresult = yat.yahtzee_scoring(test_lst)
    assert(expected_result == actualresult)


#unit tests-------------------------------------------
