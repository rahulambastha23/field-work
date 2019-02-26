#CLASS A
timeTable_4A = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]

subjectwise_faculty_4A = {"CSA":"Aakanksha Choubey","DS":"Samta Gajbhiye","DMS":"Manjula Swarnakar","OS":"Megha Mishra","CM":"K.K. Pandey","OOPS":"Rajesh Tiwari", "H/W LAB":"Aakanksha Choubey", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Rajesh Tiwari"}

class_4A_faculty_details = [
    ["OS", 7, 3, 3.5, 8],
    ["CSA", 8, 2.5, 1.5, 7],
    ["DS", 8, 2, 2.5, 10],
    ["CM", 9, 2, 3.5, 8],
    ["DMS", 8, 1, 1, 6],
    ["OOPS", 7, 3, 2, 7],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

#CLASS B
timeTable_4B = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DM', 'OS', 'OOPS LAB', 'OOPS LAB', 'B', 'CM', 'OOPS', 'CSA'],
    ['TUE', 'OS', 'DM', 'DS', 'CSA', 'R', 'OOPS', 'GUI LAB', 'GUI LAB'],
    ['WED', 'OOPS', 'CM', 'OS', 'DM', 'E', 'DS', 'DS LAB', 'DS LAB'],
    ['THU', 'DS', 'CSA', 'H/W LAB', 'H/W LAB', 'A', 'OS', 'CM', 'OOPS'],
    ['FRI', 'CM', 'OS', 'OOPS', 'CSA', 'K', 'DM', 'DS', 'DS'],
]

subjectwise_faculty_4B = {"OOPS":"Abhishek Dewangan","OS":"Megha Mishra", "CM":"K.K. Pandey", "DMS":"Yogesh Sahu", "DS":"Yamini Chouchan", "CSA":"Kamal Mehta", "H/W LAB":"Kamal Mehta", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Abhishek Dewangan"}

class_4B_faculty_details = [
    ["OS", 7, 3, 3.5, 8],
    ["CSA", 8, 1, 3.5, 10],
    ["DS", 3, 0, 3.5, 6],
    ["CM", 9, 2, 3.5, 8],
    ["DMS", 5, 1, 3.5, 5],
    ["OOPS", 10, 3.5, 3.5, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

#CLASS C
timeTable_4C = [
    ['Day', 'Lecture 1', 'Lecture 2', 'Lecture 3', 'Lecture 4', '', 'Lecture 5', 'Lecture 6', 'Lecture 7'],
    ['MON', 'DS', 'DS', 'DMS', 'CMS', 'B', 'OOPS', 'H/W LAB', 'H/W LAB'],
    ['TUE', 'CM', 'CSA', 'DS LAB', 'DS LAB', 'R', 'DM', 'OOPS', 'OS'],
    ['WED', 'CSA', 'OOPS', 'DS', 'DS', 'E', 'OS', 'DM', 'CM'],
    ['THU', 'OOPS', 'CSA', 'DM', 'CM', 'A', 'OS', 'DS', 'DS'],
    ['FRI', 'OS', 'OOPS', 'OOPS LAB', 'OOPS LAB', 'K', 'CSA', 'CM', 'DM'],
]
subjectwise_faculty_4C = {"DS":"Siddharth Choubey", "CSA":"Aakanksha Choubey", "CM":"Yogesh Sahu", "DMS":"Manjula Swarnakar", "OS":"Megha Mishra", "OOPS":"Abhishek Dewangan", "H/W LAB":"Prageet Vajpayee", "GUI LAB":"Sampada Massey", "OOPS LAB":"Abhishek Dewangan"}

class_4C_faculty_details = [
    ["OS", 7, 3, 3.5, 8],
    ["CSA", 8, 2.5, 1.5, 7],
    ["DS", 10, 1, 4, 10],
    ["CM", 5, 1, 3.5, 5],
    ["DMS", 8, 1, 1, 6],
    ["OOPS", 10, 3.5, 3.5, 9],
    ["H/W LAB", 0, 0, 0, 0],
    ["GUI LAB", 0, 0, 0, 0],
    ["OOPS LAB", 0, 0, 0, 0]
]

# Print TT
def printTable(table):
    for i in range(0, 6):
        for j in range(0, 9):
            print('{:^18}'.format(table[i][j]), end = "")
        print("\n")
    print("\n\n\n")
