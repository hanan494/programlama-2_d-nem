miktar=int(input("kg giriniz:"))
if miktar<=10:
    islem=miktar*10
    print ("ödeme:",islem)
else:
    ucret=100+(miktar-10)*7.5
    print("ödeme:",ucret)