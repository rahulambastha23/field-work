count = 0
store_occurences = []  # Stores all lecture indices in selected row for that faculty
for j in temp:
    if count == 0 or count == 5:
        count += 1
    else:
        if faculty_dict[j] == faculty_name:
            store_occurences.append(count)
        count += 1
print(store_occurences)
copyTT = tt
counter2 = -1
for i in copyTT:
    if i[0] == day:
        for j in i:
            if i.index(j) in store_occurences:
                copyTT[copyTT.index(i)][i.index(j)] = "X"
    break

# display(copyTT)
