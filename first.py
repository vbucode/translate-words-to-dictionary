from translit import Translit

xlist = []
ylist = []
xstring = ""

with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            xlist.append(line.replace("\n", ""))

for i in xlist:
    t = Translit(i.lower())
    tl = t.load()
    if len(ylist) == 0:
        xvar = "|" + tl + "-" + i.lower() + "|"
    else:
        xvar = tl + "-" + i.lower() + "|"
    ylist.append(xvar)

xstring = "".join(ylist)

with open("translit-origin.txt", "a") as file2:
    file2.write("{}".format(xstring))
