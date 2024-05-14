#class and constructor

class Calisan:

    zam_orani = 1.8 #class variable
    counter = 0

    def __init__(self,isim,soyisim,maas): #constructor
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email= isim + " " + soyisim+"@asd.com"

        Calisan.counter = Calisan.counter +1

    def giveNameSurname(self):
        return self.isim + " " + self.soyisim

    def zam_yap(self):
        self.maas= self.maas + self.maas*self.zam_orani

#isci1 = Calisan("ali","veli",100)
#print(isci1.maas)
#print(isci1.giveNameSurname())

calisan1 = Calisan("ali","veli",100)
print("İlk maas:", calisan1.maas)
calisan1.zam_yap()
print("Yeni maas:",calisan1.maas)
calisan2 = Calisan("merve","ayse",400)
print(calisan2.isim)
print(Calisan.counter)

calisan2 = Calisan("ayse","hatice",200)
calisan3 = Calisan("ayse","yelda",600)
calisan4 = Calisan("ali","veli",500)

liste = [calisan1,calisan2,calisan3,calisan4]

maxi_maas= -1
i = -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas =each.maas
        i = each
print(maxi_maas)
print(i.giveNameSurname())




