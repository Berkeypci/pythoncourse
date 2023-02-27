# #%% substring
mesaj = "Merhaba dünya"
# print(mesaj[2:5])
# yeniMesaj = mesaj[12:13]
# print(yeniMesaj)

# #%%  len
# print(len(mesaj))
# yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
# print(yeniMesaj2)

# #%%  lower upper
# print(mesaj.upper())
# print(mesaj.lower())

# #%%  replace
# # mesaj = mesaj.replace("Ã¼","u")
# print(mesaj.replace("ü","u"))
# print(mesaj)
# print(mesaj.replace("a","e"))

#%%  split ve strip
# bilgi = "        Berke;Yapıcı;20;Kırklareli ".strip()
# bilgi2 = "        Berke;Yapıcı;20;Kırklarlei"
# print(bilgi)
# print(bilgi2)

# print(bilgi.split(";"))

# print("Adınız = " + bilgi.split(";")[0])

#%%  input
ad = input("Adınız?")
sayi1 = input("Soyad 1 =? ")
sayi2 = input("Soyad 2 =? ")
print(int(sayi1) + int(sayi2))



