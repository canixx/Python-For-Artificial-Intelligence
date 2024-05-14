#for= range var

for each in range(1,11):
    print(each)

for each in "ankara ist":
    print(each)

for each in "ankara ist".split(): #splitin içine birşey atamadık defauşt değerini kullanıyoruz. kelimeleri boşluklarına göre ayır demek.
    print(each)

#way1
liste = [1,4,5,6,8,3,3,4,67]
summation= sum(liste)
print(summation)

#way 2
count=0
for each in liste:
    count = count +each
    print(count)

#while=condition var

#first
i=0
while(i<4):
    print(i)
    i=i+1
#second
limit= len(liste)
each = 0
count=0
while (each < limit):
    count = count+ liste[each]
    each = each+1
print(count)

# liste verecegim
#sizden bu listenin icindeki en kucuk sayiyi bulmanizi istiyorum

liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

mini = 100000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue
print(mini)