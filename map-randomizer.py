import glob, random

diffname = input("diffname query: ")
change = int(input("change how much?: "))

path = glob.glob(('*'+diffname+'*.osu'))[0]
path2 = path[:-5] + " - randomized by " + str(change) + "].osu"
print("input path: " + path)
print("output path: " + path2)

f = open(path,'r+')
f2 = open(path2,'a')

wiersze = f.readlines()

# diffname change
i=0
while (wiersze[i].find("Version:") == -1):
    i+=1

wiersze[i] = wiersze[i][:-2] + " - randomized by " + str(change) + "\n"

# separate the hitobject rows
while (wiersze[i].find("[HitObjects]") == -1):
    i+=1

hitobjects = wiersze[i+1:]
wiersze = wiersze[:i+1]

# append the non-hitobject rows to new file
f2.writelines(wiersze)

# modify the hitobject rows and append them to new file
for wiersz in hitobjects:
    xd = wiersz.replace(",","x",1)
    comma1 = xd.find("x")
    comma2 = xd.find(",")

    x = int(wiersz[0 : comma1])
    y = int(wiersz[comma1+1 : comma2])

    x += random.randint(-change,change)
    y += random.randint(-change,change)

    nowywiersz = str(x) + "," + str(y) + wiersz[comma2:]
    f2.write(nowywiersz)

f2.close()
f.close()