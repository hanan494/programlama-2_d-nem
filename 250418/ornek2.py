sure=int(input("otoparta kaç saat kaldınız:"))
if sure==1:
    print("5 TL")
elif sure>=1 and sure<=5:
    print("4 TL")
else:
    print("3 TL", sure *4)        
    