fr = open("slova.txt", "r", encoding = "UTF-8")
ise = 0
isnote = 0
for row in fr:
    temp = row.strip()
    if temp.count("e") >= 1:
        ise += 1
    else:
        isnote += 1
print(ise,"\n",isnote)
