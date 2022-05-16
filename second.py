import re

xlist = []
ylist = []
llist = []
llist2 = []
rlist = []
rlist2 = []

with open("translit-origin.txt", "r") as file:
    f = file.read()

ylist = re.split("\|", f)

for i in ylist:
    try:
        lat, org, *res = i.split("-")
    except ValueError:
        continue
    llist.append(lat)
    rlist.append(org)

with open("translit-translated.txt", "r") as file2:
    f2 = file2.read()

xlist = re.split("\|", f2)

for i in xlist:
    try:
        lat2, trd, *res = i.split("-")
    except ValueError:
        continue
    llist2.append(lat2)
    rlist2.append(trd)


with open("dictionary.txt", "a") as file3:
    for i in llist:
        for j in llist2:
            if i == j:
                file3.write("{}:{}\n".format(rlist2[llist2.index(j)], rlist[llist.index(i)]))

