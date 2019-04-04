import json

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]["grade_breakdown"]
    return grades

def OldGrades():
    k=input('do you want to make any changes? please answer in yes or no.' )
    if k == 'yes':
        return MAIN()
    else:
        print('Okey, you can change it whenever you want:)')

def askForAssignmentMarks(grades):
    current_grades = {"mygrades": {}}

    for key in grades:
        print(grades[key])
        current_grades["mygrades"][key] = input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")

    return current_grades

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades):
    curr_grade = 0
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = int(current_grades["mygrades"][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print (curr_grade)

def MAIN():
    grades = loadSetupData()
    current_grades = askForAssignmentMarks(grades)
    saveGrades(current_grades)
    printCurrentGrade(grades, current_grades)
    
def Check():
    with open('gc_grades.json') as data:
        oldinput = json.load(data)
    
    if oldinput["mygrades"] == "":
        return MAIN()
    else:
        a= open('gc_grades.json','r')
        line=a.readline()
        print (line[0:-1])
        return OldGrades()
        a.close()
Check()
        
    
