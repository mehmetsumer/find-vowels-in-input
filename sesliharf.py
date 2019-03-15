# -*- coding: utf-8 -*-
def calistir():
    sesli_harf="aeıioöuü"
    tut=[0,0,0,0,0,0,0,0]
    cumle = input("Giriş= ") 
    toplam=0
    for i in range(0,len(cumle)):
        for j in range(len(sesli_harf)):
            if cumle[i] == sesli_harf[j]:
                tut[j]+=1
    for i in range(len(tut)):
        if tut[i]!=0:
            print (sesli_harf[i] , ": ",tut[i]) 
            toplam+= tut[i]
    print("Toplam: ",toplam)
    
calistir()
bekle=input("")