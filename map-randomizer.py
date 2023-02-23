# put this file in the desired song folder and run it
# type 1 - change the x and y values by a random number
# type 2 - move at a random angle by the given distance (not sure if it works)

import glob, random, math

randomtype = input("type (1 or 2): ")
diff = input("diff: ")
change = int(input("change how much?: "))

path = glob.glob(('*'+diff+'*.osu'))[-1]
path2 = path[:-5] + " - randomized by " + str(change) + "].osu"
print("input path: " + path)
print("output path: " + path2)

f = open(path, errors="ignore")
f2 = open(path2,'a')

wiersze = f.readlines()

# diffname change
i=0
while (wiersze[i].find("Version:") == -1):
    i+=1

wiersze[i] = wiersze[i][:-1] + " - randomized by " + str(change) + "\n"

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

    if (randomtype == 1):
        x += random.randint(-change,change)
        y += random.randint(-change,change)
    else:
        x += math.cos( random.randint(0,359) ) * change
        y += math.sin( random.randint(0,359) ) * change

    nowywiersz = str(x) + "," + str(y) + wiersz[comma2:]
    f2.write(nowywiersz)

f2.close()
f.close()