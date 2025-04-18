k1=int(input("1.kenarı giriniz:"))
k2=int(input("2.kenarı giriniz:"))
k3=int(input("3.kenarı giriniz:"))
if k1==k2 and k2==k3:
    print("üçgen eşkenar")
elif k1==k2 or k2==k3 or k3==k3:    
    print("üçgen ikizkenar")
else:
    print("üçgen çeşit kenar ")    