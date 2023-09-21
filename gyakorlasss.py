#1.f kérjunk be a felhasznalotol 2 egesz szamto es vizgs meg melyik nagyobb?es ha ket ertek pontos ugyanannyi
#2.f bekerunk 5 egesz szamot mindegyik megv h pozitiv v negativ ill. 20-nál nagyobb v kisebb+számold meg hány olyan ami pozitív és 20-nál nagyobb
"""
szam1=int(input("adj meg egy egesz szamot:"))
szam2=int(input("adj meg még egy egész számot:"))
if szam1 < szam2:
    print("a második szám:", szam2 ,"a nagyobb")
if szam1 > szam2:
    print("az első szam:", szam1 , "a nagyobb")
elif szam1 == szam2:
    print("a két szám ugyan annyi")
"""

szam1=int(input("adj meg egy egész szamot:"))
szam2=int(input("adj meg egy egész szamot:"))
szam3=int(input("adj meg egy egész szamot:"))
szam4=int(input("adj meg egy egész szamot:"))
szam5=int(input("adj meg egy egész szamot:"))

if szam1 > 0:
    print("az első megadott szam pozitív")
if szam1 < 0:
    print("az első megadott szam negatív")
if szam1 > 20:
    print("az első szám nagyobb 20-nál")
if szam1 < 20:
    print("az első szám kisebb 20-nál")
if szam2 > 0:
    print("az második megadott szam pozitív")
if szam2 < 0:
    print("a második megadott szam negatív")
if szam2 > 20:
    print("a második szám nagyobb 20-nál")
if szam2 < 20:
    print("a második szám kisebb 20-nál")
if szam3 > 0:
    print("az harmadik megadott szam pozitív")
if szam3 <0:
    print("az harmadik megadott szam negatív")
if szam3 > 20:
    print("a harmadik szám nagyobb 20-nál")
if szam3 < 20:
    print("a harmadik szám kisebb 20-nál")
if szam4 > 0:
    print("az negyedik megadott szam pozitív")
if szam4 < 0:
    print("az negyedik megadott szam negatív")
if szam4 > 20:
    print("a negyedik szám nagyobb 20-nál")
if szam4 < 20:
    print("a negyedik szám kisebb 20-nál")
if szam5 > 0:
    print("az ötödik megadott szam pozitív")
if szam5 < 0:
    print("az ötödik megadott szam negatív")
if szam5 > 20:
    print("a ötödik szám nagyobb 20-nál")
if szam5 < 20:
    print("a ötödik szám kisebb 20-nál")

szam = 0

if szam1 > 20:  
    szam + 1
if szam2 > 20:
    szam + 1
if szam3 > 20:
     szam + 1
if szam4 > 20:
    szam + 1
if szam5 > 20:
    szam + 1
print("ennyi pozitív és nagyobb 20-nál", szam)
    
    



