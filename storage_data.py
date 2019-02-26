login={"CSELECT01":["0001","Kamal Mehta"],"CSELECT02":["0002","Akanksha Choubey"],"CSELECT03":["0003","Abhishek Dewangan"],
       "CSELECT04":["0004","Rajesh Tiwari"],"CSELECT05":["0005","Krishna Kumar Pandey"],"CSELECT06":["0006","Manjula Swarnkar"],
       "CSELECT07":["0007","Yamini Chauhan"], "CSELECT08":["0008","Siddharth Choubey"], "CSELECT09":["0009","Samta Gajbhiye"],
       "CSELECT10": ["0010", "Yogesh Kumar Sahu"], "CSELECT11":["0011","Megha Mishra"], "CSELECT12":["0012","Vishnu Mishra"],
       "CSELECT13": ["0013", "Sampada Massey"], "CSELECT14":["0014","Prageet Vajpayee"]}


#CLASS A
timeTable_4A = [
    ['MON', 'DS', 'DS', 'CSA', 'OOPS', 'B', 'OS', 'CM', 'DMS'],
    ['TUE', 'CSA', 'OOPS', 'H/W LAB', 'H/W LAB', 'R', 'OS', 'DMS', 'CM'],
    ['WED', 'OOPS', 'OS', 'OOPS LAB', 'OOPS LAB', 'E', 'DS', 'DMS', 'CSA'],
    ['THU', 'OS', 'OOPS', 'DMS', 'DS', 'A', 'CM', 'DS LAB', 'DS LAB'],
    ['FRI', 'DMS', 'CSA', 'CM', 'DS', 'K', 'OOPS', 'GUI LAB', 'GUI LAB'],
]
subjectwise_faculty_4A = {"CSA":"Aakanksha Choubey","DS":"Samta Gajbhiye","DMS":"Manjula Swarnakar","OS":"Megha Mishra","CM":"K.K. Pandey","OOPS":"Rajesh Tiwari", "H/W LAB":"Aakanksha Choubey", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Rajesh Tiwari"}

#CLASS B
timeTable_4B = [
    ['MON', 'DM', 'OS', 'OOPS LAB', 'OOPS LAB', 'B', 'CM', 'OOPS', 'CSA'],
    ['TUE', 'OS', 'DM', 'DS', 'CSA', 'R', 'OOPS', 'GUI LAB', 'GUI LAB'],
    ['WED', 'OOPS', 'CM', 'OS', 'DM', 'E', 'DS', 'DS LAB', 'DS LAB'],
    ['THU', 'DS', 'CSA', 'H/W LAB', 'H/W LAB', 'A', 'OS', 'CM', 'OOPS'],
    ['FRI', 'CM', 'OS', 'OOPS', 'CSA', 'K', 'DM', 'DS', 'DS'],
]

subjectwise_faculty_4B = {"OOPS":"Abhishek Dewangan","OS":"Megha Mishra", "CM":"K.K. Pandey", "DMS":"Yogesh Sahu", "DS":"Yamini Chouchan", "CSA":"Kamal Mehta", "H/W LAB":"Kamal Mehta", "GUI LAB":"Vishnu Mishra", "OOPS LAB":"Abhishek Dewangan"}

#CLASS C
timeTable_4C = [
    ['MON', 'DS', 'DS', 'DMS', 'CMS', 'B', 'OOPS', 'H/W LAB', 'H/W LAB'],
    ['TUE', 'CM', 'CSA', 'DS LAB', 'DS LAB', 'R', 'DM', 'OOPS', 'OS'],
    ['WED', 'CSA', 'OOPS', 'DS', 'DS', 'E', 'OS', 'DM', 'CM'],
    ['THU', 'OOPS', 'CSA', 'DM', 'CM', 'A', 'OS', 'DS', 'DS'],
    ['FRI', 'OS', 'OOPS', 'OOPS LAB', 'OOPS LAB', 'K', 'CSA', 'CM', 'DM'],
]
subjectwise_faculty_4C = {"DS":"Siddharth Choubey", "CSA":"Aakanksha Choubey", "CM":"Yogesh Sahu", "DMS":"Manjula Swarnakar", "OS":"Megha Mishra", "OOPS":"Abhishek Dewangan", "H/W LAB":"Prageet Vajpayee", "GUI LAB":"Sampada Massey", "OOPS LAB":"Abhishek Dewangan"}


#login form

#2nd page
def display(tt):
    for i in range(0, 5):
        for j in range(0, 9):
            print('{:^18}'.format(tt[i][j]), end = "")
        print("\n")
    print("\n\n\n")

def secondpage():
    section= 'A'
    day="TUE"
    teacher_logged_in = "Aakanksha Choubey"
    if section=='A':
        display(timeTable_4A)
        access(timeTable_4A,day,subjectwise_faculty_4A, teacher_logged_in)
    elif section=='B':
        display(timeTable_4B)
        access(timeTable_4B, day, subjectwise_faculty_4B, teacher_logged_in)
    else:
        display(timeTable_4C)
        access(timeTable_4C, day, subjectwise_faculty_4C, teacher_logged_in)


def access(tt, day, faculty_dict, faculty_name):
    for row in  tt:
        if row[0]==day:
            temp = row[0:]         #that particular days tt
            print(temp)
            break
    count = 0
    store_occurences = []               #Stores all lecture indices in selected row for that faculty
    for j in temp:
        if count==0 or count==5:
            count+=1
        else:
            if  faculty_dict[j] == faculty_name:
                store_occurences.append(count)
            count += 1
    print(store_occurences)
    copyTT = tt
    counter2 = -1
    for i in copyTT:
        if i[0] == day:
            for j in store_occurences:
                i[j] = "X"

    display(copyTT)


secondpage()