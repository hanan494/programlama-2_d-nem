toplam=0
s1=int(input("1.sayıyı giriniz:"))
s2=int(input("2.sayıyı giriniz:"))
for i in range(s1,s2):
    toplam=toplam+i
adet=s2-s1
ortalama=toplam/adet
print(ortalama)