hash_table = {}
season_ht = {"Fall":50, "Winter":30, "Spring":50, "Summer":70}
print(season_ht["Fall"])
season_ht["Winter"] = 50
print(season_ht)

print("Winter" in season_ht)

def is_person_in_company(person_years_ht, person):
    if person in person_years_ht:
        age = person_years_ht[person]
        print("The teammate named " + person + " has been at the company for " + str(age) + " years.")

if __name__ == "__main__":
    employee_years_ht = {"Christian": 1, "Ryan": 1, "Alex": 25, "Ernesto": 20}

    is_person_in_company(employee_years_ht, "Christian")

#HW: 1) Make a hash table mapping each family members name (and last initial if same name) to a list of all the jobs they've ever had. Implement a function that takes in a family job hash table and a job to search for and return a list of family members who have had that job before
#HW: 2) Make a hash table mapping each job to the list of family members who have had that job. Implement a function that takes in the hash table and a job name and return a list of all the family members who have completed that job
#HW: Note: make sure to have 6-7 different jobs and make up a scenario where there are multiple family members who have done different jobs

#Extra Credit: write a function that takes in a set of strings and a search string and returns true or false depending on whether that search string is in the set or not