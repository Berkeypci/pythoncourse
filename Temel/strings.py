# #%% substring
mesaj = "Merhaba d�nya"
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
# # mesaj = mesaj.replace("ü","u")
# print(mesaj.replace("�","u"))
# print(mesaj)
# print(mesaj.replace("a","e"))

#%%  split ve strip
# bilgi = "        Berke;Yap�c�;20;K�rklareli ".strip()
# bilgi2 = "        Berke;Yap�c�;20;K�rklarlei"
# print(bilgi)
# print(bilgi2)

# print(bilgi.split(";"))

# print("Ad�n�z = " + bilgi.split(";")[0])

#%%  input
ad = input("Ad�n�z?")
sayi1 = input("Soyad 1 =? ")
sayi2 = input("Soyad 2 =? ")
print(int(sayi1) + int(sayi2))



