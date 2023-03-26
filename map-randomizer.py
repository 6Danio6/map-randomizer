# put this file in the desired song folder and run it
# method 1 - change the x and y values of each circle by a random number
# method 2 - move each circle at a random angle by the given distance

import glob, random, math

method = input("method (1 or 2): ")
diff = input("difficulty name: ")
change = int(input("change amount (10 to 50 is recommended): "))

diffchange = " - random=" + str(change) + " method=" + str(method)

path = glob.glob(('*'+diff+'*.osu'))[-1]
path2 = path[:-5] + diffchange + "].osu"
print("input path: " + path)
print("output path: " + path2)

f = open(path, errors="ignore")
f2 = open(path2,'a')

wiersze = f.readlines()

# diffname change
i=0
while (wiersze[i].find("Version:") == -1):
    i+=1

wiersze[i] = wiersze[i][:-1] + diffchange + "\n"

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

    if (method == 1):
        x += random.randint(-change,change)
        y += random.randint(-change,change)
    else:
        angle = math.radians( random.randint(0,359) )
        x += math.cos(angle) * change
        y += math.sin(angle) * change

    nowywiersz = str(x) + "," + str(y) + wiersz[comma2:]
    f2.write(nowywiersz)

f2.close()
f.close()