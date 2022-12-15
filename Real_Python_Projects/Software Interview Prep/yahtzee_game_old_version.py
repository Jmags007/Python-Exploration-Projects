#creating the Yahtzee game in this file
#rulesvbased off of https://cardgames.io/yahtzee/
#13 rounds
#roll dice (5 dice)

#put score in one of 13 categories
#must score once in each category

#scoring:
#upper scores
#ones (add all of that number together)
#twos (add all of that number together)
#threes (add all of that number together)
#fours (add all of that number together)
#fives (add all of that number together)
#sixes (add all of that number together)

#lower scoring
#three of a kind (sum of all dice not just the three of a kind)
#four of a kind (sum of all dice not just the three of a kind)
#full house (score 25 points)
#small straight (ex:1,2,3,4) (score 30 points)
#large straight (ex:1,2,3,4,5) (score 40 points)
#chance (score: sum of all the dice)
#yahtzee (5 of a kind) (score 50 points)

#multiple Yahtzees
#if you already have a yahtzee score for yahtzee goes up to 100
#you can also then put the socre for the yahtzee in a different category
#if you already have marked 0 for yahtzee then you cant get a yahtzee

#put in the source for the rules-----------------------------------------
#------------------------------------------------------------------------

#things to add-----------------------------------------------------------
#better to use hashtable instead of pprint
#do all edge cases for unit tests
#while loo p to determine if th user is done
#changed rules for double yahtzee can keep on rolling yahtzees
#multiple rolls (up to 3) for the scoring

#reason for having a hash table, it can quickly determine if they have already socred there.
#key is the string like large straight

#change 


import random
from pprint import pprint
import Yahtzee_game_unit_tests
from threading import Lock

#defs ------------------------------------------------
def roll_dice(n):
    dice = []
    for die in range(n):
        dice.append(random.randint(1,6))
    return dice

#still needs a uniut test for this assign_dice
def print_dice(lst):
    for i in range(len(lst)):
        dice_number = i + 1
        print(f"d{dice_number}=>", lst[i])


def calculate_dice_roll_for_selection(dice_roll_lst, user_selection_int):
    if user_selection_int > 0 and user_selection_int <= 6:
        score = upper_scoring(dice_roll_lst, user_selection_int)
    if user_selection_int == 7:
        score = three_of_a_kind_scoring(dice_roll_lst)
    if user_selection_int == 8:
        score = four_of_a_kind_scoring(dice_roll_lst)
    if user_selection_int == 9:
        score = full_house_scoring(dice_roll_lst)
    if user_selection_int == 10:
        score = small_straight_scoring(dice_roll_lst)
    if user_selection_int == 11:
        score = large_straight_scoring(dice_roll_lst)
    if user_selection_int == 12:
        score = chance_scoring(dice_roll_lst)
    if user_selection_int == 13:
        score = yahtzee_scoring(dice_roll_lst)
    return score

def upper_scoring(dice_roll_selection_lst, user_selection_integer):
    count = 0
    for i in dice_roll_selection_lst:
        if i == user_selection_integer:
            count += i
    return count

def three_of_a_kind_scoring(dice_roll_list):
    count = 0
    for i in range(1,6):
        if dice_roll_list.count(i) >= 3:
            for die in dice_roll_list:
                count += die
    return count

def four_of_a_kind_scoring(dice_roll_list):
    count = 0
    for i in range(1,6):
        if dice_roll_list.count(i) >= 4:
            for die in dice_roll_list:
                count += die
    return count

def full_house_scoring(dice_roll_list):
    print("this is the full_house_scoring function (dice_roll_list)", dice_roll_list)
    count = 0
    two_of_a_kind_flag = False
    three_of_a_kind_flag = False
    for i in range(1,6):
        if dice_roll_list.count(i) == 2:
            two_of_a_kind_flag = True
            print("two_of_a_kind_flag", two_of_a_kind_flag)
        if dice_roll_list.count(i) == 3:
            three_of_a_kind_flag = True
            print("three_of_a_kind_flag", three_of_a_kind_flag)
        print("this is i in the for loop", i)
    if two_of_a_kind_flag == True and three_of_a_kind_flag == True:
        count = 25
    return count

def small_straight_scoring(dice_roll_list):
    dice_roll_list.sort()
    count = 0
    for i in range(len(dice_roll_list) - 1):
        if dice_roll_list[i + 1] == (dice_roll_list[i] + 1):
            count += 1
        elif dice_roll_list[i + 1] == dice_roll_list[i]:
            count = count
        else:
            count = 0
        #if three in a row break loop 
        if count == 3:
            break
    if count == 3:
        score = 30
    else:
        score = 0
    return score

def large_straight_scoring(dice_roll_list):
    dice_roll_list.sort()
    count = 0
    for i in range(len(dice_roll_list) - 1):
        if dice_roll_list[i + 1] == (dice_roll_list[i] + 1):
            count += 1
        elif dice_roll_list[i + 1] == dice_roll_list[i]:
            count = count
        else:
            count = 0
        #if four in a row break loop 
        if count == 4:
            break
    if count == 4:
        score = 50
    else:
        score = 0
    return score

def chance_scoring(dice_roll_list):
    return sum(dice_roll_list)

def yahtzee_scoring(dice_roll_list):
    if dice_roll_list.count(dice_roll_list[0]) == 5:
        score = 50
    else:
        score = 0
    return score



if __name__=="__main__":
    #check unit tests first
    Yahtzee_game_unit_tests.unit_tests()

    #initalize socre card
    score_card = [[1, "Ones", None], [2, "Twos", None], [3, "Threes", None], [4, "Fours", None], [5, "Fives", None], [6, "sixes", None],
    [7, "Three of a kind", None], [8, "Four of a kind", None], [9, "Full house", None], [10, "Small straight", None], [11, "Large straight", None], 
    [12, "Chance", None], [13, "Yahzee", None]]

    #create a lock
    lock = Lock()


    #13 rounds
    for i in range(13):
        #show the scorecard
        pprint(score_card)

        #show what the user rolled
        n = 5
        dice_roll = roll_dice(n)
        print("you rolled:")
        print_dice(dice_roll)

        #while loop to determine the dice roll-----------------
        three_rolls_flag = True
        number_of_dice_roll = 0
        continous_dice_roll_flag = True
        while three_rolls_flag == True:

            #check for double yahtzee
            if dice_roll.count(dice_roll[0]) == 5 and score_card[12][2] == 50:
                print("ayyyy lets go you get an additional 50 for hitting another yahtzee")
                score_card[12][2] = score_card[12][2] + 100

            #ask user if they would like to roll again
            flag = True
            while flag:
                check_roll_again = input("would you like to roll again? (type 'y' for yes and 'n' for no): ")
                if check_roll_again == 'y':
                    flag = False
                elif check_roll_again == 'n':
                    flag = False
                    continous_dice_roll_flag = False
                else:
                    print("something went wrong, make sure to only put integers")

            #check to see if user wanted to stop rolling early through continous_dice_roll_flag
            if continous_dice_roll_flag == False:
                break

            #ask the user if they want to pick some dice to keep and roll the rest--------------
            #bruv you need to do a check to make sure they dont but in some wack numbers-----------------------------------------------------
            flag = True
            while flag:
                dice_to_re_roll = input("which dice would you like to re-roll (ex: 531) : ")
                try:
                    int(dice_to_re_roll)
                    flag = False
                except:
                    flag = True
                    continue
                #check to make sure length of string does not exceed 5 dice
                if len(dice_to_re_roll) > 5:
                    flag = True
                #check to make sure there arent double of the smae digits
                for i in dice_to_re_roll:
                    if dice_to_re_roll.count(i) > 1:
                        flag = True
                    #check to make sure integers are 1 thru 6 only
                    if int(i) < 1 or int(i) > 5:
                        flag = True
                if flag == True:
                    print("something went wrong, make sure to only put integers")

            #re-roll the selected dice
            #remove the dice from the dice_roll string (will concadinate later) (should probably do a dictonary for dice roll)
            for i in sorted(dice_to_re_roll, reverse=True):
                del dice_roll[int(i)-1]

            #re-roll the dice need to create a more general rolling dice function as well as---------------
            #concadinate the dice we have with the re-rolled dice
            n = len(dice_to_re_roll)
            new_dice_roll = roll_dice(n) + dice_roll
            dice_roll = new_dice_roll
            print("your new roll is:")
            print_dice(dice_roll)

            #count how many times you have rolled before 
            number_of_dice_roll += 1

            #check to see if the user has rolled 3 times already for the round
            if number_of_dice_roll == 3:
                three_rolls_flag = False
            

        #dice_roll = [3, 2, 3, 2, 3]
        #print("this is the dice roll", dice_roll)

        #ask to pick what the user wants and check if valid
        flag = True
        while flag:
            try:
                user_selection = int(input("type the number associated with the score name you want to select for this roll: "))
                if user_selection > 0 and user_selection < 14 and score_card[user_selection - 1][2] == None:
                    flag = False
            except:
                print("something went wrong, try again")
            if flag == True:
                print("something went wrong, try again")

        lock.acquire()
        #calculate score and add to score card
        score_card[user_selection - 1][2] = calculate_dice_roll_for_selection(dice_roll, user_selection)
        lock.release()
        
    #print out the score_card one last time
    pprint(score_card)
    #print out what your score was
    score_totaled = []
    for each_score in score_card:
        score_totaled.append(each_score[2])
    players_score = sum(score_totaled)
    print("your score is:", players_score)


    