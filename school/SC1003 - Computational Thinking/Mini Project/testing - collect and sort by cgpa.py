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

def main():
    details = collect()
    details.append("Team")

    with open("teams.csv", "w") as file:
        file.write(",".join(details) + "\n")
        
    for key in cohort:
        cgpa_list = cgpasort(key)
        print(cgpa_list)

main()
