# Belajar Elif => else if

menu_pilihan = input("Silahkan pilih menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda memilih menu 1")
elif menu_pilihan == "2":
    print("Anda memilih menu 2")
elif menu_pilihan == "3":
    print("Anda memilih menu 3")
else:
    print("Menu tidak tersedia")

if menu_pilihan == "x":
    print("Program keluar")






    
print("==============")


print("1. nasi ayam kremes 12k")
print("2. pakai sayur dan ayam pop 12k")
print("3. pakai rendang 15k")
print("4. nasi kakap 25k ")

menu=int(input("masukan pilihan nasi padang : "))
if menu == 1:
    print("harga 12k bayar dikasir")
elif menu == 2:
    print("bayar 12k dengan ayam pop")
elif menu == 3:
    print("bayar 15k karena dengan rendang")
elif menu == 4:
    print ("bayar 25k dengan kakap")
else:
    print("tidak ada menu itu")
    
if menu == 4-100:
    print("keluar dari program") 
