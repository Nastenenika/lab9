filename = "data.csv"
def get_data(fn):
    with open (fn) as file:
        lines = file.readlines()
    return lines
lines = get_data(filename)
sum_liave = 0
sum_dead = 0
i = 0
for line  in lines:
    if i < 1:
        i += 1
        continue
    tmpR = line.strip().rsplit(",",8)
    tmp = line.strip().split(",",3)
#подсчет выживших и погибших
    who = 0
    if tmp[1].isdigit():
        who = int(tmp[1])
    SibSp = 0
    if tmpR[3].isdigit():
        SibSp = int(tmpR[3])
    Parch = 0
    if tmpR[4].isdigit():
        Parch = int(tmpR[4])
#Сумма выживших и погибших родственников
    if who == 0:
        sum_dead = sum_dead + SibSp + Parch
    if who == 1:
        sum_liave = sum_liave + SibSp + Parch
print("Родственников у погибших: {}".format(sum_dead))
print("Родственников у выживших: {}".format(sum_liave))
