#merge sort
#time complexity O:nlog(n), log(n) from the spliting and n for the merging
#recurisve in nature
def merge_sort(arry):
    #print("made it to recusion")
    #check to determine if your at the final element so you dont have keep splitting
    if len(arry) != 1:

        #split into a left side and right side
        middle_index = len(arry)//2
        L = arry[:middle_index]
        R = arry[middle_index:]
        #print("this is L:", L)
        #print("this is R:", R)
        #print("going into left side merge_sort")
        left_arry = merge_sort(L)
        #print("going into right side merge_sort")
        right_arry = merge_sort(R)

        #start sorting each layer going up
        i = j = k = 0
        
        #print("this is len(arry):", len(arry))
        #print("this is the left arry:", left_arry)
        #print("this is the right arry:", right_arry)
        while k < len(arry):
            #print("this is i:", i)
            #print("this is j:", j)
            #print("this is k:", k)
            if i < len(left_arry) and j < len(right_arry):
                if left_arry[i] <= right_arry[j]:
                    #print("1")
                    arry[k] = left_arry[i]
                    i += 1
                else:
                    #print("2")
                    arry[k] = right_arry[j]
                    j += 1
            else:
                if i == len(left_arry):
                    #print("3")
                    arry[k] = right_arry[j]
                    j += 1
                else:
                    #print("4")
                    arry[k] = left_arry[i]
                    i += 1
            k += 1
    #print("this is the arry at the end of merge_sort", arry)
    return arry

#insertion sort
#time complexity: worst case O:n^2, best case O:n (its already sorted)
def insertion_sort(arry):

    #go thorugh each index
    for i in range(1, len(arry) - 2):

        #index of number being sorted
        sorted_number_index = i

        #index for numbers being compared
        left_number_index = sorted_number_index - 1

        #while loop until its placed correctly
        flag = True
        while flag == True:
            if arry[left_number_index] > arry[sorted_number_index]:
                #update arry
                number_holder = arry[left_number_index]
                arry[left_number_index] = arry[sorted_number_index]
                arry[sorted_number_index] = number_holder
                #change the indexing for next go around
                left_number_index -= 1
                sorted_number_index -= 1
            else:
                flag = False
            
            #check if at the last index
            if left_number_index < 0:
                flag = False
    return arry



if __name__ == "__main__":
    '''
    print("hell ya we made it")
    arry = [1, 2, 3, 4, 5]
    middle = len(arry)//2
    print(middle)
    left_arry = arry[:middle]
    right_arry = arry[middle:]
    print(left_arry)
    print(right_arry)
    '''
    unsorted_arry = [3, 5, 2, 4, 1, 8, 6, 9, 7]
    print(merge_sort(unsorted_arry))
    print(insertion_sort(unsorted_arry))

    