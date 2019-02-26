#CLASS A
timeTable_4A = [
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]

subjectwise_faculty_4A = {"CSA":"Aakanksha Choubey","DS":"Samta Gajbhiye","DMS":"Manjula Swarnakar","OS":"Megha Mishra","CM":"K.K. Pandey","OOPS":"Rajesh Tiwari", "H/W LAB":"Aakanksha Choubey", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Rajesh Tiwari"}

# Course Completion, Skill, Load hour, Experience
class_4A_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 2.5, 1.5, 8, 7],
    ["DS", 2, 2.5, 8, 10],
    ["CM", 2, 3.5, 9, 8],
    ["DMS", 1, 1, 8, 6],
    ["OOPS", 3, 2, 7, 7],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

#CLASS B
timeTable_4B = [
    ['MON', 'DM', 'OS', 'OOPS LAB', 'OOPS LAB', 'B', 'CM', 'OOPS', 'CSA'],
    ['TUE', 'OS', 'DM', 'DS', 'CSA', 'R', 'OOPS', 'GUI LAB', 'GUI LAB'],
    ['WED', 'OOPS', 'CM', 'OS', 'DM', 'E', 'DS', 'DS LAB', 'DS LAB'],
    ['THU', 'DS', 'CSA', 'H/W LAB', 'H/W LAB', 'A', 'OS', 'CM', 'OOPS'],
    ['FRI', 'CM', 'OS', 'OOPS', 'CSA', 'K', 'DM', 'DS', 'DS'],
]

subjectwise_faculty_4B = {"OOPS":"Abhishek Dewangan","OS":"Megha Mishra", "CM":"K.K. Pandey", "DMS":"Yogesh Sahu", "DS":"Yamini Chouchan", "CSA":"Kamal Mehta", "H/W LAB":"Kamal Mehta", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Abhishek Dewangan"}

class_4B_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 1, 3.5, 8, 10],
    ["DS", 0, 3.5, 3, 6],
    ["CM", 2, 3.5, 9, 8],
    ["DMS", 1, 3.5, 5, 5],
    ["OOPS", 3.5, 3.5, 10, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

#CLASS C
timeTable_4C = [
    ['MON', 'DS', 'DS', 'DMS', 'CMS', 'B', 'OOPS', 'H/W LAB', 'H/W LAB'],
    ['TUE', 'CM', 'CSA', 'DS LAB', 'DS LAB', 'R', 'DM', 'OOPS', 'OS'],
    ['WED', 'CSA', 'OOPS', 'DS', 'DS', 'E', 'OS', 'DM', 'CM'],
    ['THU', 'OOPS', 'CSA', 'DM', 'CM', 'A', 'OS', 'DS', 'DS'],
    ['FRI', 'OS', 'OOPS', 'OOPS LAB', 'OOPS LAB', 'K', 'CSA', 'CM', 'DM'],
]
subjectwise_faculty_4C = {"DS":"Siddharth Choubey", "CSA":"Aakanksha Choubey", "CM":"Yogesh Sahu", "DMS":"Manjula Swarnakar", "OS":"Megha Mishra", "OOPS":"Abhishek Dewangan", "H/W LAB":"Prageet Vajpayee", "GUI LAB":"Sampada Massey", "OOPS LAB":"Abhishek Dewangan"}

class_4C_faculty_details = [
    ["OS", 3, 3.5, 7, 8],
    ["CSA", 2.5, 1.5, 8, 7],
    ["DS", 1, 4, 10, 10],
    ["CM", 1, 3.5, 5, 5],
    ["DMS", 1, 1, 8, 6],
    ["OOPS", 3.5, 3.5, 10, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

def preference(tt,subject_faculty,temp):
    counter=0
    for i in tt:
        for j in range(9):
            if j in temp:
                if   i.count(i[j])>3:
                    i[j]= subject_faculty[1][0]
                else:
                    i[j] = subject_faculty[0][0]
        break
    print(i)
# Print TT
def printTable(table):
    for i in range(0, 6):
        for j in range(0, 9):
            print('{:^18}'.format(table[i][j]), end = "")
        print("\n")
    print("\n\n\n")

preference(timeTable_4C, class_4C_faculty_details, [1, 3, 6])
