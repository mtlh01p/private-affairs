import random
cohort = {}

# collect students information from the csv file and includes it from the
def collect():
    global cohort
    with open('records.csv', "r") as namelist:
        details = namelist.readline().split(",")
        details[-1] = details[-1].strip("\n")
        for person in namelist:
            student = person.split(",") # splits the string into a list of information. Elements to be split is determined through the position of the comma
            student[-1] = float(student[-1].strip("\n")) # removes the newline behind the CGPA value and transforms it into a float
            if student[0] not in cohort:
                tutgrp = {}
                cohort.update({student[0]:tutgrp})

            personaldetails = {
                                details[1] : student[1],
                                details[2] : student[2],
                                details[4] : student[4],
                                details[5] : student[5]
                            }
            tutgrp.update({student[3]:personaldetails})
    return details

def cgpasort(tutorialgroup):
    studentcgpa = [[cohort[tutorialgroup][student]["CGPA"], student] for student in cohort[tutorialgroup]]
    studentcgpa.sort() #sort priortises the cgpa of the students as it is the first element in the nested loop
    return studentcgpa

def createteams(numberofteams, cgpa, tutorialgroup):
    # creates the desired number of teams
    teams = [0 * n for n in range(numberofteams)]

    # calculates the average CGPA of the tutorial group
    sumofcgpa = 0
    for student in cgpa:
        sumofcgpa += student[0]
    averagecgpa = sumofcgpa / len(cgpa)

    # Adds in the first two members of the group into the team by pairing the top x with bottom x students (x being the number of teams)
    for i in range(numberofteams):
        teams[i] = [cgpa[i][1], cgpa[-i-1][1]] # Adds a student with the highest gpa and lowest gpa into each team.
        #1st element is CGPA then student name

    # reorganises the remaining students into a dictionary called leftover. Students are sorted according to cgpa, school and then gender
    leftover = reorganise(teams, averagecgpa, tutorialgroup) # makes a new dictionary which contains the names of the students reorganised according to cgpa, school and gender

    #this dictionary stores the key information (gender, school and average cgpa) of teams at any point of time.
    teaminfo = {team: gatherinfo(teams[team], tutorialgroup) for team in range(len(teams))}

    # adds the next 2 or 3 members for each of the team. This is done one member by one member for each team to ensure better diversity.
    for members in range(0,3):
        for teamnumber in range(0, len(teams)):
            # organises members into different priority levels depending on how well they suit the team. This will be done for the addition of each member to the team to make sure there is
            # better diversity
            potentialmembers = findmembers(teaminfo[teamnumber], averagecgpa, leftover, tutorialgroup, teams[teamnumber])

            # skims through each of the priority levels. If a priority level does not have any members (ie: There is no "Most suitable" student), looksfor the next best one
            for prioritylevel in potentialmembers:
                if len(prioritylevel) != 0:
                    randomstudent  = random.randint(0, len(prioritylevel)-1)
                    teams[teamnumber].append(prioritylevel[randomstudent])
                    # removes the new member from the leftover dictionary. This is because the program continuously recalculates who is good for the team with each new member added in.
                    removestudent(prioritylevel[randomstudent], leftover, tutorialgroup, averagecgpa)
                    break
                else:
                    continue
    return teams

def main():
    details = collect()
    details.append("Team")

    with open("teams.csv", "w") as file:
        file.write(",".join(details) + "\n")
        
    for key in cohort:
        cgpa_list = cgpasort(key)
        numberofteams = 10

        # creates the teams within the tutorial group
        teams = createteams(numberofteams, cgpa_list, key)

main()
