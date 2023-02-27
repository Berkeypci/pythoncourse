
 #%%
# sehir = "Ankara"

# sonuc = sehir.upper()
# print(sonuc)
# print(sehir.endswith("e"))

#%%
# def selamVer(isim = "ziyaretçi"):
#     print("Merhaba " + isim)
    
# selamVer("Berke")
# selamVer("Derin")
# selamVer("Salih")
# selamVer("Ahmet")
# selamVer("Mehmet")
# selamVer()

# def selamVer2(isim ="Sayın", soyIsim ="arkadaş"):
#     print("Merhaba " + isim + " " + soyIsim)

# selamVer2("Sedef")
# selamVer2("Berke","Yapıcı")
# selamVer2()
 #%%
# def dikUcgenAlaniHesapla(a,b):
#     return a*b/2

# alan = dikUcgenAlaniHesapla(2,3)

# print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(4,5))


