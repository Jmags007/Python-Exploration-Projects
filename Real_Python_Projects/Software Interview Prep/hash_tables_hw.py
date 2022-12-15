#HW: 1) Make a hash table mapping each family members name (and last initial if same name) 
# to a list of all the jobs they've ever had. Implement a function that takes in a family 
# job hash table and a job to search for and return a list of family members who have had that job before
#HW: 2) Make a hash table mapping each job to the list of family members who have had that job.
#  Implement a function that takes in the hash table and a job name and return a list of 
# all the family members who have completed that job
#HW: Note: make sure to have 6-7 different jobs and make up a scenario where there are 
# multiple family members who have done different jobs

#Extra Credit: write a function that takes in a set of strings and a search string and 
# returns true or false depending on whether that search string is in the set or not
#---------------------------------------------------------------------------------------------------

def find_family_members_with_job(family_dict, job_title):
    #create lst to store family members
    family_members_with_job = []
    #iterate through family members
    for family_member in family_dict:
        #iterate through family members jobs
        for job in family_dict[family_member]:
            #see if job_title is in family members jobs
            if job_title == job:
                #if job_title in family members jobs
                family_members_with_job.append(family_member)
    return family_members_with_job

def reverse_key_value_ht(family_dict):
    #create lst with all family members
    unique_lst_of_family_members = []
    for family_member in family_dict:
        unique_lst_of_family_members.append(family_member)
    
    #print(unique_lst_of_family_members)

    #create a lst with all jobs
    unique_lst_of_jobs = []
    #iterate through family members
    for family_member in family_dict:
        #iterate through family members jobs
        for job in family_dict[family_member]:
            #if job not in jobs list add job
            if (job in unique_lst_of_jobs) == False:
                unique_lst_of_jobs.append(job)

    #print(unique_lst_of_jobs)

    #initialize dictonary
    jobs_family_members_ht = {}
    #iterate through unique list of jobs
    for job in unique_lst_of_jobs:
        #create a list of people that have that job title & add list of family members with job to dictionary
        jobs_family_members_ht[job] = find_family_members_with_job(family_dict, job)
        
    return jobs_family_members_ht

#Extra credit---------------------------------------------------------------
def search_for_string_in_set(set_of_strings, search_string):
    flag = False
    for string in set_of_strings:
        if string == search_string:
            flag = True
    if flag == True:
        print(search_string + " is in the set of strings")
    else:
        print(search_string + " is not in the set of strings")
#Extra credit---------------------------------------------------------------

if __name__ == "__main__":
    #intialize family (key) job (value) hash table
    family_member_job_ht = {
        "mom":["accountant", "iron worker", "healthcare worker"],
        "dad":["iron worker", "strawberry picker"],
        "gianna":["server", "customer service"],
        "debby":["DMV","accountant"],
        "desiree":["care taker"],
        "pete":["car sales men"],
        "dylan":["plaid pantery", "car sales men"],
        "orion":["cart pusher"],
        "john":["cart pusher", "delivery driver", "mechatronics engineer", "computer programmer", "iron worker"]
    }

    print(find_family_members_with_job(family_member_job_ht, "iron worker"))
    #print(reverse_key_value_ht(family_member_job_ht))
    job_family_member_ht = reverse_key_value_ht(family_member_job_ht)
    print(find_family_members_with_job(job_family_member_ht, "mom"))

    #extra credit------------------------------------------------------
    #intialize set of strings
    random_set = {"12345", "vibes", "funny", "12kj2h34", "sun", "car", "ballon"}
    search_for_string_in_set(random_set, "12345")
    #extra credit------------------------------------------------------
