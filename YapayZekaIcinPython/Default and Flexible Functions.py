# default
# çemberin çevresi = 2*pi*r

def cember_cevresi_hesapla(r,pi = 3.14): #pi'ye 3.114 atadık yani default ettik. r=2 derken bir daha pi'ye 3.14 dememize gerek kalmaz.
                                         #default parametreler sona yazılır
    """
    cember cevresi hesaplama
    input(parametre)= r, pi
    output = çemberin çevresi
    """

    output= 2*pi*r
    return output
print(cember_cevresi_hesapla(2))


#filexible
def hesapla(boy,kilo):
    output = boy+kilo
    return output
print(hesapla(175,62))

#def hesapla(boy,kilo,yas):
#    output = (boy + kilo)*yas
#    return output
#print(hesapla(175,62,22))

def hesapla(boy,kilo,*args): #args= daha sonradan eklenebilecek parametreler için.
    print(len(args))
    output = boy+kilo
    return output
print(hesapla(1,2))

def hesapla(boy,kilo,*args): #args= daha sonradan eklenebilecek parametreler için.
    print(args)
    output = boy+kilo
    return output
print(hesapla(1,2,5))

def hesapla(boy,kilo,*args): #args= daha sonradan eklenebilecek parametreler için.
    print(args)
    output = boy+kilo
    return output
print(hesapla(1,2,5,4,5,3,4)) #böyle oldugunda işleme argsın ilk elementi yani 5'i dahil eder.

def hesapla(boy,kilo,*args): #args= daha sonradan eklenebilecek parametreler için.
    print(args)
    output = (boy+kilo)*args[3] #böyle oldugunda ise seçtiğimiz args indeksini işleme dahil eder.
    return output
print(hesapla(1,2,5,4,5,3,4))